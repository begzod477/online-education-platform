from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='education/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='education/logout.html'), name='logout'),  
    path('add_course/', views.add_course, name='add_course'),
    path('profile/', views.profile, name='profile'), 
]
