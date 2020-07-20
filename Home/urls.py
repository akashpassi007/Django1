from django.contrib import admin
from django.urls import path

from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home Page'),
    path('about', views.about, name='About Page'),
    path('services', views.services, name='Services page'),
    path('contact', views.contact, name='Contact page')
]
