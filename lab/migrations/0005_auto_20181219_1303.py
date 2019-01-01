# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-19 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20181218_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='asa',
        ),
        migrations.AddField(
            model_name='post',
            name='microscope',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u041c\u0438\u043a\u0440\u043e\u0441\u043a\u043e\u043f'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=500, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0442\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0442\u0438\u0438'),
        ),
    ]