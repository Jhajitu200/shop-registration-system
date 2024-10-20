# Shops/forms.py

from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'latitude', 'longitude']

    def clean_latitude(self):
        lat = self.cleaned_data['latitude']
        if not (-90 <= lat <= 90):
            raise forms.ValidationError("Invalid latitude value")
        return lat

    def clean_longitude(self):
        lon = self.cleaned_data['longitude']
        if not (-180 <= lon <= 180):
            raise forms.ValidationError("Invalid longitude value")
        return lon
