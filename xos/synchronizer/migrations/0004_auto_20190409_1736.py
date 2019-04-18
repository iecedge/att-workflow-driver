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

# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-09 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att-workflow-driver', '0003_auto_20190312_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attworkflowdriverserviceinstance',
            name='dhcp_state',
            field=models.CharField(choices=[(b'AWAITING', b'Awaiting'), (b'DHCPDISCOVER', b'DHCPDISCOVER'), (b'DHCPACK', b'DHCPACK'), (b'DHCPREQUEST', b'DHCPREQUEST')], default=b'AWAITING', max_length=256),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverserviceinstance',
            name='of_dpid',
            field=models.CharField(help_text=b'OLT Openflow ID', max_length=256),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverserviceinstance',
            name='onu_state',
            field=models.CharField(choices=[(b'AWAITING', b'Awaiting'), (b'ENABLED', b'Enabled'), (b'DISABLED', b'Disabled')], default=b'AWAITING', help_text=b'ONU administrative state', max_length=256),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverserviceinstance',
            name='serial_number',
            field=models.CharField(help_text=b'Serial number of ONU', max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverserviceinstance',
            name='status_message',
            field=models.CharField(blank=True, default=b'', help_text=b'Status text of current state machine state', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverwhitelistentry',
            name='serial_number',
            field=models.CharField(help_text=b'ONU Serial Number', max_length=256),
        ),
    ]