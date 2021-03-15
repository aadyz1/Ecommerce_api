from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.
class ListCatagory(generics.ListCreateAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer
class DetailCatagory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer
class ListBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer