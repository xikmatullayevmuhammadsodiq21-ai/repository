
from django.shortcuts import render


# Create your views here.

def home_page(request):
    return render(request, "index.html")


def about_page(request):
    return render(request, 'about-us.html')

def contact_page(request):
    return render(request, 'contact-us.html')


def our_page(request):
    return render(request, 'our-services.html')