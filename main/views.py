from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

def home(request):
    return HttpResponse("<h1>Fluxaa Api is running.</h1>")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer