from django.forms import forms
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
