from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="shop-home"),
    path('about/', views.about, name="about-us"),
    path('contact/', views.contact, name="contact-us"),
    path('tracker/', views.tracker, name="tracking-status"),
    path('search/', views.search, name="search"),
    path('productview/', views.productView, name="prod-view"),
    path('checkout/', views.checkout, name="checkout"),
]