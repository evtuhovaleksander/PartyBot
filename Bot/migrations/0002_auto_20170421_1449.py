# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 14:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='actual',
            field=models.BooleanField(default=True, verbose_name='actual'),
        ),
        migrations.AddField(
            model_name='day',
            name='date',
            field=models.DateField(default=datetime.date(1, 1, 1), verbose_name='date'),
        ),
    ]
