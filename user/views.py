from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')

    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    form = AuthenticationForm()
    context = {
        'form': form
    }

    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')
@login_required(login_url='login')
def profile_view(request):
    return render(request, 'profile.html')