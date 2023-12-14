from django import forms
from .models import icecream

class iceform(forms.ModelForm):
    class Meta:
        model=icecream
        fields=['name','desc','price','img']


