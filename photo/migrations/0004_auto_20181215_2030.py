# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-15 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20181215_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='country',
            field=models.CharField(blank=True, max_length=50, verbose_name='원산지'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, verbose_name='상품 설명'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=50, verbose_name='상품명'),
        ),
    ]
