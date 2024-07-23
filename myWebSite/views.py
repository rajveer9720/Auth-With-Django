from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,EditUSerProfileForm,AdminProfileForm
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
# Create your views here.
#For sign up Form
def sign_up(request):
 if request.method == "POST":
  fm = SignUpForm(request.POST)
  if fm.is_valid():
   fm.save()
   messages.success(request,'Account Has been create successfully')
  #  return HttpResponseRedirect('/login/')

 else:
   fm = SignUpForm()
 return render(request,'myWebSite/signup.html',{'form':fm})

#Login View
def User_login(request):
 if not request.user.is_authenticated:
  if request.method == 'POST':
    fm = AuthenticationForm(request=request, data = request.POST)
    if fm.is_valid():
     uname = fm.cleaned_data['username']
     upass = fm.cleaned_data['password']
     user = authenticate(username =uname,password =upass)
     if user is not None:
       login(request,user)
       messages.success(request,'to Your Profile ')
       return HttpResponseRedirect('/profile/')
  else:
    fm =AuthenticationForm()
  
  return render(request, 'myWebSite/login.html', {'form':fm})
 else:
  return HttpResponseRedirect('/profile/')

   
#For User Profile
def profile(request):
 if request.user.is_authenticated:
  if request.method == "POST":
   if request.user.is_superuser == True:
    fm = AdminProfileForm(request.POST, instance=request.user)
    users = User.objects.all()
   else:
    fm = EditUSerProfileForm(request.POST, instance=request.user)
    users =None
   if fm.is_valid():
    messages.success(request,'Your Profile Updated Successfully. !!!')
    fm.save()
  else:
   if request.user.is_superuser == True:
    fm = AdminProfileForm(instance=request.user)

   else:
    fm =EditUSerProfileForm(instance = request.user)
  return render(request,'myWebSite/simpleprofile.html',{'name':request.user,'form':fm,'user':User})
 else:
   return HttpResponseRedirect('/login')

#User Logout 
def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/login/')


#chnage Password with old password

def change_pass(request):
  if request.user.is_authenticated: 
    if request.method =="POST":
      fm =PasswordChangeForm(user=request.user,data=request.POST)
      if fm.is_valid():
       fm.save()
      messages.info(request,'Password Changed Successfully')
      update_session_auth_hash(request,fm.user)
      return HttpResponseRedirect('/profile/')
    else:
      fm = PasswordChangeForm(user=request.user) 
    return render(request,'myWebSite/change.html',{'form':fm})
  else:
   return HttpResponseRedirect('/login/')

def change_pass1(request):
  if request.user.is_authenticated: 
    if request.method =="POST":
      fm =SetPasswordForm(user=request.user,data=request.POST)
      if fm.is_valid():
       fm.save()
      messages.info(request,'Password Changed Successfully')
      update_session_auth_hash(request,fm.user)
      return HttpResponseRedirect('/profile/')
    else:
      fm = SetPasswordForm(user=request.user) 
    return render(request,'myWebSite/change.html',{'form':fm})
  else:
   return HttpResponseRedirect('/login/')