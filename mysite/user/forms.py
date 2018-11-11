from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from phone_field import PhoneField

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone = PhoneField(blank=True, help_text='Contact phone number')

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
