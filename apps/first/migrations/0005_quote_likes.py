# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-24 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_auto_20180724_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='likes',
            field=models.ManyToManyField(related_name='likesT', to='first.User'),
        ),
    ]
