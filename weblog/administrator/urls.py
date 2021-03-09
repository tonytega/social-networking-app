"""administrator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from user import urls as user_urls
from django.contrib.flatpages import urls as flatpage_url
from django.urls import path,re_path,include
from pages import pages_url
from .administrator_views import redirect_root
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from pages.views import HomePage,LogingClass,LogoutView

urlpatterns = [
    path(r'accounts/profile/',HomePage.as_view()),
    path(r'login/',LogingClass.as_view(),name='login'),
    path(r'logout/',LogoutView.as_view(),name='logout'),
    path(r'',LogingClass.as_view(),name='login'),
    path('user/',include(user_urls)),
    path(r'admin/', admin.site.urls),
    re_path(r'^home|HOME/$',redirect_root),
    path(r'site/',include(pages_url)),
    path(r'flat',include(flatpage_url)),
]
