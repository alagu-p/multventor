from django.shortcuts import render
from . import serializers
from rest_framework import generics,permissions
from . import serializers
from . import models

# Create your views here.
class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    #basic authentication
    # permission_classes = [permissions.IsAuthenticated]
class VendorDetail(generics.RetrieveUpdateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]
class ProductList(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer
