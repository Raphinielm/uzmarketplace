from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

products = Products.objects.all


def home(request):
    return HttpResponse("WELCOME TO THE HOME PAGE")


def index(request):
    return render(request, 'index.html', {'products': products})
# Create your views here.
