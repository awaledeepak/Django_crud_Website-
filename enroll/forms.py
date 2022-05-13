from django.core import validators 
from django import forms
from .models import User 

class StudentRegistration(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['name', 'email', 'phone' , 'address', 'password']  
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}), 
            'address': forms.TextInput(attrs={'class':'form-control'}), 
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),  
            
        }
