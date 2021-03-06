from django import forms
from django.forms import ModelForm
from . import models

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class PurchaseOrderForm(ModelForm):
    class Meta: 
        model = models.OrderDetail
        fields = ['productName', 'productDescription', 'deliveryAddress','quantity', 'orderDate']