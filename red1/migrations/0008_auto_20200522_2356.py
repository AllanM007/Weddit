# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-05-22 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red1', '0007_auto_20200519_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=20, null=True),
        ),
    ]