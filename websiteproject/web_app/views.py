from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def adminpage(request):
    return render(request, 'adminpage.html')
# Create your views here.
