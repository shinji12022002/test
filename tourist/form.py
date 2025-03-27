

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Booking  # Make sure you import your Booking model

# Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Login Form (using Django's built-in AuthenticationForm)
class LoginForm(AuthenticationForm):
    pass

# Booking Form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'email', 'phone_number', 'tour_name', 'booking_date', 'special_requirements']
