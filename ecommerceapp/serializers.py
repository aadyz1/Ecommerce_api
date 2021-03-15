from rest_framework import serializers
from .models import *

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Catagory
        fields=(
            'id',
            'title'
        )
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=(
            'id',
            'catagory',
            'author',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageurl',
            'status',
            'date_created'
        )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=(
            'id',
            'product_tag',
            'name',
            'catagory',
            'price',
            'stock',
            'imageurl',
            'status',
            'date_created'
        )