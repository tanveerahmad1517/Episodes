# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshow', '0003_auto_20160725_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
