from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContinentSerializer, CountrySerializer, CitySerializer, DateWeatherSerializer
from .models import Continent, Country, City, DateWeather
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from django.db.models import Prefetch

# Create your views here.

class ContinentListAll(APIView):
    def get(self, request, format=None):
        continents = Continent.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(serializer.data)





class ContinentList(viewsets.ViewSet):
    def list(self, request, continent_name=None):
        queryset = Continent.objects.all()
        user = get_object_or_404(queryset, continent_name=continent_name)
        serializer = ContinentSerializer(user)
        return Response(serializer.data)

    def retrieve(self, request, continent_name=None, country_name=None, city_name=None):
        if country_name and city_name:
            queryset = Continent.objects.filter(continent_name=continent_name).prefetch_related(
                Prefetch("country", queryset=Country.objects.filter(
                    country_name=country_name).prefetch_related(
                    Prefetch('city', queryset=City.objects.filter(city_name=city_name)))
                )
            )

        else:
            queryset = Continent.objects.filter(continent_name=continent_name).prefetch_related(
                Prefetch("country", queryset=Country.objects.filter(
                    country_name=country_name))
            )
        serializer = ContinentSerializer(queryset, many=True)

        return Response(serializer.data)





class CountryList(APIView):
    def get(self, request, format=None):
        countrys = Country.objects.all()
        serializer = CountrySerializer(countrys, many=True)
        return Response(serializer.data)




class CityList(APIView):
    def get(self, request, format=None):
        cityes = City.objects.all()
        serializer = CountrySerializer(cityes, many=True)
        return Response(serializer.data)


class DateWeatherList(APIView):
    def get(self, request, format=None):
        weathers = DateWeather.objects.all()
        serializer = CountrySerializer(weathers, many=True)
        return Response(serializer.data)