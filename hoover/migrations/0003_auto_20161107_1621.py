# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoover', '0002_remove_hoover_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoover',
            name='nvmid',
            field=models.CharField(max_length=50),
        ),
    ]
