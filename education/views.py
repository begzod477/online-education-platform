from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import Course, Student

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akkount muvaffaqiyatli yaratildi: {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'education/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Siz tizimga muvaffaqiyatli kirdingiz!')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'education/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Siz tizimdan muvaffaqiyatli chiqdingiz!')
    return redirect('home')

@login_required  
def home(request):
    courses = Course.objects.all()  
    return render(request, 'education/home.html', {'courses': courses})

@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kurs muvaffaqiyatli qo\'shildi!')
            return redirect('home')
    else:
        form = CourseForm()
    return render(request, 'education/add_course.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'education/profile.html', {'user': request.user})
