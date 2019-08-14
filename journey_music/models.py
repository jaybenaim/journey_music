from django.db import models 
from django.forms import ModelForm 
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date 
from django import forms 



class Trip(models.Model): 
    location = models.CharField(max_length=255)
    weather = models.CharField(max_length=255)

    def __str__(self): 
        return f'Trip to {self.location}'


class Track(models.Model): 
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, related_name='tracks')
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self): 
        return f'{self.artist} - {self.track}'
        