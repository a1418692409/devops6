# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-08 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180107_0532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='book',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='book',
            name='createtime',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='updatetime',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]