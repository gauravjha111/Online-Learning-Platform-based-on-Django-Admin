# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-23 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20170621_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='head'),
        ),
    ]