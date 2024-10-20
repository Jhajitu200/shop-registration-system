# Shops/views.py

from django.shortcuts import render, redirect
from .forms import ShopForm
from .models import Shop
import haversine as hs
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ShopSerializer

def register_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_list')
    else:
        form = ShopForm()
    return render(request, 'Shops/register.html', {'form': form})

def search_shops(request):
    user_lat = float(request.GET.get('latitude'))
    user_lon = float(request.GET.get('longitude'))
    
    user_location = (user_lat, user_lon)
    shops = Shop.objects.all()

    shop_distances = []
    for shop in shops:
        shop_location = (shop.latitude, shop.longitude)
        distance = hs.haversine(user_location, shop_location)
        shop_distances.append((shop, distance))

    sorted_shops = sorted(shop_distances, key=lambda x: x[1])
    return render(request, 'Shops/shop_list.html', {'shops': sorted_shops})

@api_view(['GET'])
def api_shop_list(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_search_shops(request):
    user_lat = float(request.GET.get('latitude'))
    user_lon = float(request.GET.get('longitude'))
    user_location = (user_lat, user_lon)

    shops = Shop.objects.all()
    shop_distances = []

    for shop in shops:
        shop_location = (shop.latitude, shop.longitude)
        distance = hs.haversine(user_location, shop_location)
        shop_distances.append((shop, distance))

    sorted_shops = sorted(shop_distances, key=lambda x: x[1])
    sorted_shops_data = [{'name': shop.name, 'distance': dist} for shop, dist in sorted_shops]
    
    return Response(sorted_shops_data)
