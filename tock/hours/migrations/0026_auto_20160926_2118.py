# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0025_auto_20160926_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportingperiod',
            name='target_billable_hours',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
