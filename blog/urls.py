"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from notes import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^contact/',views.contact, name='contact'),
    url(r'^research/', views.research, name='research'),
    url(r'^publications/', views.publications, name='publications'),
    url(r'^projects/', views.project, name='projects'),
    url(r'^essays/', views.essays, name='essays'),
    url(r'^diaries/', views.diaries, name='diaries'),
    url(r'^how-tos/', views.how_tos, name='how-tos'),
    url(r'^poems/', views.poems, name='poems'),
    url(r'^trips/', views.trips, name='trips'),
    url(r'^random/', views.random, name='random'),
]
