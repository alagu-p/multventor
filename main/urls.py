from django.utils import http
from django.urls import path
from .import views
urlpatterns =[
    path('vendors/', views.VendorList .as_view()),
    path('vendor/<int:pk>/  ', views.VendorDetail.as_view()),
    path('product/', views.ProductList .as_view()),
    path('product/<int:pk>', views.ProductList .as_view()),
]