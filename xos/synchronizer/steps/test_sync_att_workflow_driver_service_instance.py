# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import functools
from mock import patch, call, Mock, PropertyMock
import requests_mock
import multistructlog
from multistructlog import create_logger

import os, sys

# Hack to load synchronizer framework
test_path=os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
xos_dir=os.path.join(test_path, "../../..")
if not os.path.exists(os.path.join(test_path, "new_base")):
    xos_dir=os.path.join(test_path, "../../../../../../orchestration/xos/xos")
    services_dir = os.path.join(xos_dir, "../../xos_services")
sys.path.append(xos_dir)
sys.path.append(os.path.join(xos_dir, 'synchronizers', 'new_base'))
# END Hack to load synchronizer framework

# generate model from xproto
def get_models_fn(service_name, xproto_name):
    name = os.path.join(service_name, "xos", xproto_name)
    if os.path.exists(os.path.join(services_dir, name)):
        return name
    else:
        name = os.path.join(service_name, "xos", "synchronizer", "models", xproto_name)
        if os.path.exists(os.path.join(services_dir, name)):
            return name
    raise Exception("Unable to find service=%s xproto=%s" % (service_name, xproto_name))
# END generate model from xproto

class TestSyncAttWorkflowDriverServiceInstance(unittest.TestCase):

    def setUp(self):

        self.sys_path_save = sys.path
        sys.path.append(xos_dir)
        sys.path.append(os.path.join(xos_dir, 'synchronizers', 'new_base'))

        # Setting up the config module
        from xosconfig import Config
        config = os.path.join(test_path, "../test_config.yaml")
        Config.clear()
        Config.init(config, "synchronizer-config-schema.yaml")
        # END Setting up the config module

        from synchronizers.new_base.mock_modelaccessor_build import build_mock_modelaccessor
        build_mock_modelaccessor(xos_dir, services_dir, [
            get_models_fn("att-workflow-driver", "att-workflow-driver.xproto"),
            get_models_fn("olt-service", "volt.xproto"),
            get_models_fn("../profiles/rcord", "rcord.xproto")
        ])
        import synchronizers.new_base.modelaccessor

        from sync_att_workflow_driver_service_instance import SyncAttWorkflowDriverServiceInstance, model_accessor

        # import all class names to globals
        for (k, v) in model_accessor.all_model_classes.items():
            globals()[k] = v


        self.sync_step = SyncAttWorkflowDriverServiceInstance

        self.oss = AttWorkflowDriverService()
        self.oss.name = "oss"
        self.oss.id = 5367

        # create a mock AttWorkflowDriverServiceInstance instance
        self.o = Mock()
        self.o.serial_number = "BRCM1234"
        self.o.of_dpid = "of:109299321"
        self.o.pon_port_id = 1
        self.o.owner.leaf_model = self.oss
        self.o.tologdict.return_value = {}

        self.pon_port = PONPort(
            port_no=1
        )
        self.onu = ONUDevice(
            serial_number=self.o.serial_number,
            pon_port=self.pon_port
        )

    def tearDown(self):
        self.o = None
        sys.path = self.sys_path_save

    def test_sync_valid(self):
        with patch.object(AttWorkflowDriverWhiteListEntry.objects, "get_items") as whitelist_items, \
            patch.object(ONUDevice.objects, "get_items") as onu_items:
            # Create a whitelist entry for self.o's serial number
            whitelist_entry = AttWorkflowDriverWhiteListEntry(
                owner_id=self.oss.id,
                serial_number=self.o.serial_number,
                device_id=self.o.of_dpid,
                pon_port_id=1,
            )
            whitelist_items.return_value = [whitelist_entry]
            onu_items.return_value = [self.onu]

            self.sync_step().sync_record(self.o)

            self.assertEqual(self.o.valid, "valid")
            self.o.save.assert_called()

    def test_sync_bad_location(self):
        with patch.object(AttWorkflowDriverWhiteListEntry.objects, "get_items") as whitelist_items, \
            patch.object(ONUDevice.objects, "get_items") as onu_items:
            # Create a whitelist entry for self.o's serial number
            whitelist_entry = AttWorkflowDriverWhiteListEntry(
                owner_id=self.oss.id,
                serial_number=self.o.serial_number,
                device_id="foo",
                pon_port_id=666
            )
            whitelist_items.return_value = [whitelist_entry]
            onu_items.return_value = [self.onu]

            self.sync_step().sync_record(self.o)

            self.assertEqual(self.o.valid, "invalid")
            self.o.save.assert_called()

    def test_sync_no_whitelist(self):
        self.sync_step().sync_record(self.o)

        self.assertEqual(self.o.valid, "invalid")
        self.o.save.assert_called()

if __name__ == '__main__':
    unittest.main()
