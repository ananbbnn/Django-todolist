from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    message = ''
    username = ''
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if not user:
            message = '帳號或密碼錯誤!'
        else:
            login(request, user)
            message = '登入成功!'
            return redirect('todolist')
        
        



    return render(request, 'user/login.html', {'message':message, 'username':username})




def user_register(request):
    message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("POST!",request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(username,password1,password2)

        if password1 != password2:
            message = '兩次密碼不同!'
        elif len(password1) < 8:
            message = '密碼過短'
        else:
            user = User.objects.filter(username=username)
            if user:
                message = '使用者已存在!'
            else:
                user = User.objects.create_user(username=username,password=password1)
                user.save()
                message = '註冊成功'
                return redirect('login')





    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form':form ,'message':message}) 