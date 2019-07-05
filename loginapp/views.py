from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import auth
from .forms import *
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)  # 인증하는 함수

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패 다시 시도 ㄱ ㄱ ㄱ')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':  # request.method 가 POST방식이냐
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                                password=request.POST['password'])
            login(request, new_user)
            return redirect('index')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})


def logout(request):
    return redirect('index')
