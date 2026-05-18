from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def creaking(request):
    return render(request, 'creaking.html')

def breeze(request):
    return render(request, 'breeze.html')
# Create your views here.
