from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'template/index.html')

def juegos(request):

    return render(request, 'template/juegos.html')
