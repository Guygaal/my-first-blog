# -*- coding: utf-8 -*-
__author__ = 'User'

from django import forms

from lab.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ()


#class CronForm(forms.Form):
 #   microscope = forms.ChoiceField(label='Микроскоп', required=True, initial=None, choices=('MSPU', 'Another'))