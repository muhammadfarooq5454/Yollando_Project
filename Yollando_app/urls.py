from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shopping-sites/', views.shoppingSites, name='shoppingSites'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login, name='Login'),
    path('logout/',views.Logout,name='Logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('shippingHistory/', views.shippingHistory, name='shippingHistory'),
    path('mypackages/',views.mypackages, name='mypackages'),
    path('orderrequest/',views.orderrequest, name='orderrequest'),
    path('customerslist/', views.customerlist, name='customerslist'),
]
