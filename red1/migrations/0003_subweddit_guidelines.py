# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-05-17 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red1', '0002_auto_20200517_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='subweddit',
            name='guidelines',
            field=models.TextField(null=True),
        ),
    ]
