# Shops/urls.py

from django.urls import path
from .views import register_shop, search_shops, api_shop_list, api_search_shops

urlpatterns = [
    path('register/', register_shop, name='register_shop'),
    path('search/', search_shops, name='search_shops'),
    path('api/shops/', api_shop_list, name='api_shop_list'),
    path('api/search/', api_search_shops, name='api_search_shops'),
]
