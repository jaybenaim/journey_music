from django.db import models 
from django.forms import ModelForm 
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date 
from django import forms 
from journey_music.models import *

class TripForm(ModelForm): 
    class Meta: 
        model = Trip 
        fields = ['location']
