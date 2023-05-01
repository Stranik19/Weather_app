"""my_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('continentsAll', views.ContinentListAll.as_view()),

    path('continents/<str:continent_name>/',
        views.ContinentList.as_view({'get': 'list'})),

    path('continents/<str:continent_name>/<str:country_name>/',
        views.ContinentList.as_view({'get': 'retrieve'})),

    path('continents/<str:continent_name>/<str:country_name>/<str:city_name>/',
        views.ContinentList.as_view({'get': 'retrieve'})),


    path('continents/', views.ContinentListAll.as_view()),
    path('countrys/', views.CountryList.as_view()),
    path('cityes/', views.CityList.as_view()),
    path('weathers/', views.DateWeatherList.as_view())
]
