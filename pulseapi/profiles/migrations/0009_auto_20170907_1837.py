# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-07 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20170817_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='issues',
            field=models.ManyToManyField(blank=True, to='issues.Issue'),
        ),
    ]
