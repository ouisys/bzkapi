# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_token', '0002_auto_20160826_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cyclos_auth_string',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]