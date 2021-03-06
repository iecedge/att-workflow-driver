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
# Generated by Django 1.11.11 on 2019-03-12 22:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('att-workflow-driver', '0002_auto_20190305_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attworkflowdriverserviceinstance',
            name='authentication_state',
            field=models.CharField(choices=[(b'AWAITING', b'Awaiting'), (b'STARTED', b'Started'), (b'REQUESTED', b'Requested'), (b'APPROVED', b'Approved'), (b'DENIED', b'Denied')], default=b'AWAITING', help_text=b'Subscriber authentication state', max_length=50),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverserviceinstance',
            name='dhcp_state',
            field=models.CharField(choices=[(b'AWAITING', b'Awaiting'), (b'DHCPDISCOVER', b'DHCPDISCOVER'), (b'DHCPACK', b'DHCPACK'), (b'DHCPREQUEST', b'DHCPREQUEST')], default=b'AWAITING', max_length=254),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverserviceinstance',
            name='of_dpid',
            field=models.CharField(help_text=b'OLT Openflow ID', max_length=254),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverserviceinstance',
            name='onu_state',
            field=models.CharField(choices=[(b'AWAITING', b'Awaiting'), (b'ENABLED', b'Enabled'), (b'DISABLED', b'Disabled')], default=b'AWAITING', help_text=b'ONU administrative state', max_length=254),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverserviceinstance',
            name='serial_number',
            field=models.CharField(help_text=b'Serial number of ONU', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverwhitelistentry',
            name='backend_status',
            field=models.CharField(default=b'Provisioning in progress', max_length=1024),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverwhitelistentry',
            name='device_id',
            field=models.CharField(help_text=b'OLT Device (logical device id) on which this ONU is expected to show up', max_length=54),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverwhitelistentry',
            name='leaf_model_name',
            field=models.CharField(help_text=b'The most specialized model in this chain of inheritance, often defined by a service developer', max_length=1024),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverwhitelistentry',
            name='serial_number',
            field=models.CharField(help_text=b'ONU Serial Number', max_length=254),
        ),
        migrations.AlterField(
            model_name='attworkflowdriverwhitelistentry',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'Time this model was changed by a non-synchronizer'),
        ),
    ]
