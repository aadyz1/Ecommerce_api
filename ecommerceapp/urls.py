from django.urls import path
from .views import *
urlpatterns=[
    path('catagories/',ListCatagory.as_view(),name='catagories'),
    path('catagories/<int:pk>/',DetailCatagory.as_view(),name='single_catagory'),
path('books/',ListBook.as_view(),name='books'),
path('books/<int:pk>/',DetailBook.as_view(),name='single_book'),
path('products/',ListProduct.as_view(),name='products'),
path('products/<int:pk>/',DetailProduct.as_view(),name='single_product'),
]