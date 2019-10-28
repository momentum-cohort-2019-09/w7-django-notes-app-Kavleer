"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.notes_list, name='notes_list'), 
    path('notes/<int:pk>/', views.note_detail, name="note_detail"),
    path('notes/create/', views.note_create, name="note_create"),
    path('notes/edit/<int:pk>/', views.note_edit, name="note_edit"),
    path('notes/delete/<int:pk>/', views.note_delete, name="note_delete"),
]
