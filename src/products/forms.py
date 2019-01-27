from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(
        label='Product Title', 
        widget=forms.TextInput(
            attrs=
            {
                'Placeholder':'Product Title'
            }
        )
    )
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id",
                "rows": 5,
                "cols": 7
            }
        )
    )
    price = forms.DecimalField(initial=1.00)