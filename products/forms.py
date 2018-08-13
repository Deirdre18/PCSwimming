from django.forms import ModelForm, TextInput
from django import forms
from .models import ItemRequirements 

class ItemRequirementsForm(forms.ModelForm):
    notes = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'SIZE'}))
    
    class Meta:
        model = ItemRequirements
        fields = ['notes']