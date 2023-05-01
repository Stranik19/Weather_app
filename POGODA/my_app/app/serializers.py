from rest_framework import serializers
from  .models import Continent, Country, City, DateWeather


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ['continent_name', 'img']




class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['continent', 'country_name', 'flag']




class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['country', 'city_name']



class DateWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateWeather
        fields = ['city', 'date', 'weather_status', 'status_icon', 'wind_speed', 'humidity', 'temperature']
