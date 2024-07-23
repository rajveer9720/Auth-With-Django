from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=12)
    class Meta:
      model =User
      fields = ['username','first_name','email','phone']
      
class EditUSerProfileForm(UserChangeForm):
   password = None
   class Meta:
    model = User
    fields = ['username','first_name','last_name','email','date_joined','last_login']
    labels = {'email':'Email'}

class AdminProfileForm(UserChangeForm):
   password = None
   class Meta:
    model = User
    fields = '__all__'
    labels = {'email':'Email'}