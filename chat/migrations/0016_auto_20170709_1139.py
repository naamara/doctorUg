# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-09 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_auto_20170709_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='roles2',
        ),
        migrations.AddField(
            model_name='register',
            name='role2',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
