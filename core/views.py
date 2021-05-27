from store.views import logined
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.views import View
from store.models import *
# Create your views here.


class HomeView(View):
    def get(self , request):
        return render(request,'homepage/main.html',)

def showlogin(request):
    return render(request,'store/login.html')
def showRegister(request):
    return render(request,'store/register.html')
def logout_request(request):
    logout(request)
    return render(request,'store/login.html')
def checklogin(request):
    username=request.POST.get("username")
    password = request.POST.get("password")
    myuser = authenticate(username=username, password = password)
    context = {"warning":"Tài khoản hoặc mật khẩu không chính xác"}
    if myuser is None:
        return render(request,'store/login.html',context)
    login(request,myuser)
    return logined (myuser,request)
def register(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    repassword = request.POST.get("repassword")

    if CustomerUser.objects.filter(username = username).exists() is False:
        user = CustomerUser.objects.create_user(username=username, password=password)
        user.save()
        context = {"warning": "Đăng ký thành công"}
        return render(request,'homepage/login.html',context)
    elif(password != repassword):
        context = {"warning": "Nhập lại mật khẩu không chính xác"}
    else:
        context = {"warning": "Tài khoản đã tồn tại "}

    return render(request, 'homepage/register.html', context)