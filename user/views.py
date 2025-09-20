from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


def user_logout(request):
    logout(request)
    
    return redirect("user-login")

def user_login(request):
    message=""
    
    print(request.user)    
    
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user=authenticate(request,
                          username=username,
                          password=password)
        
        if user:
            login(request,user)
            message="登入成功!"
            return redirect("todolist")
        else:
            message = "登入失敗，帳號或密碼錯誤"
    
    return render(request,"user/login.html",{"message":message})
 

# Create your views here.
def user_register(request):
    message=""
    form=UserCreationForm()
    if request.method=="POST":
        print(request.POST)
        
        username=request.POST.get("username")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        
        user=User.objects.filter(username=username)
        if user:
            message="帳號已經存在!"        
        elif password1!=password2:
            message= "兩次密碼不相同!"
        else:
            user=User.objects.create_user(username=username,password=password1)
            user.save()
            message="註冊成功!"
        
    
    return render(request,"user/register.html",{"form":form,"message":message})