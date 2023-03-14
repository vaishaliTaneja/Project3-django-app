from django import forms
from .models import Products
#DataFlair
class ProductCreate(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'