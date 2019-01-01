# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Название партии')
    text = models.CharField(max_length=500, verbose_name='Описание партии')
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания")
    published_date = models.DateTimeField(
        default=timezone.now, blank=True, null=True, verbose_name="Дата публикации")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
