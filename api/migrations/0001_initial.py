# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('container_id', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('ip_address', models.GenericIPAddressField(protocol='IPv4')),
                ('passwd_hash', models.CharField(max_length=128, null=True)),
                ('status', models.IntegerField(null=True)),
                ('timestamp', models.TimeField(auto_now=True)),
            ],
        ),
    ]