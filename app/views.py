from django.shortcuts import render


def home(request):
    context = {'active': 'home'}
    return render(request, 'pages/home.html', context)

def about(request):
    context = {'active': 'about'}
    return render(request, 'pages/about.html', context)

def service(request):
    context = {'active': 'service'}
    return render(request, 'pages/service.html', context)

def contact(request):
    context = {'active': 'contact'}
    return render(request, 'pages/contact.html', context)