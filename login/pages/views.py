from django.shortcuts import render
from django.contrib.auth.models import User
from pages.models import UserDetails
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lg

# Create your views here.

def index (request):
     if request.user.is_authenticated:
         return render(request,"index.htm",{"User":request.user.username}) 
     return render(request,"index.htm",{})
def login(request):
     if request.method == 'GET':
          return render(request,"login.htm",{})
     elif request.method == 'POST':
          if request.POST['name'] and request.POST['password']:
               print(request.POST['name'])
               user = authenticate(username = request.POST['name'],password = request.POST['password'])
               if user != None:
                    lg(request,user)
                    if request.user.is_authenticated:
                         return render(request,"home.htm",{"User":request.user.username})
                         #return HttpResponse("<html><body><h1>Authenticated"+user.username+"!</h1></body></html>")
                         #userHome(request)
                    return HttpResponse("<html><body><h1>Successful Login"+user.username+"!</h1></body></html>")
               else:
                    return HttpResponse("<html><body><h1>Check login Credentials!</h1></body></html>")
def signup (request):
     if request.method == 'GET':
          return render(request,"signup.htm",{})
     elif request.method == 'POST':
          print("POST request")
          name = request.POST['name']
          email = request.POST['email']
          ph = request.POST['ph']
          password1 = request.POST['password1']
          password2 = request.POST['password2']
          if password1 == password2:
               user = User.objects.create_user(name,email,password1)
               if user != None:
                    print(user)
                    user = UserDetails(name = name,email = email,ph = ph)
                    user.save()
                    print("Success")
                    return HttpResponse("<html><body><h1>Success!</h1></body></html>")
          else:
               print("Passwords don't match")
               return HttpResponse("<html><body><h1>Failed Passwords don't match!</h1></body></html>")
def userlogout(request):
     logout(request)
     return render(request,"index.htm",{})