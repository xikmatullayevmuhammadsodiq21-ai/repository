from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home')
    path('', views.contact_page, name='contact')
    path('', views.our_page, name='our')
    path('', views.about_page, name='about')
]

