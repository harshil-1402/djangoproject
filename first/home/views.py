from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is home page")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is services page")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        dsc=request.POST.get('dsc')
        contact=Contact(name=name,email=email,password=password,phone=phone,dsc=dsc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
    
    #return HttpResponse("This is contact page")