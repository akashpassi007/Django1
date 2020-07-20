from django.shortcuts import render
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
# Create your views here.

from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hello world")
    #return render(request, 'index.html', {'titles': 'Akash'})
    context ={"titles":"Akash", "surname":"passi"}
    return render(request, 'index.html', context)

def about(request):
    # return HttpResponse("Welcome to profile page")
    return render(request,'about.html')


def services(request):
    # return HttpResponse("Welcome to Services page")
    return render(request,'services.html')

def contact(request):
    # return HttpResponse("Welcome to Contact page")
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!!')

    return render(request,'contact.html')
