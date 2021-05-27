from store.views import logined
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.views import View
from store.models import *
# Create your views here.


class HomeView(View):
    def get(self , request):
        return render(request,'store/main.html',)

def showlogin(request):
    return render(request,'store/login.html')
def showRegister(request):
    return render(request,'store/register.html')
def logout_request(request):
    logout(request)
    return render(request,'store/login.html')