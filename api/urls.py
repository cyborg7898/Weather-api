from .views import RegisterAPI,LoginAPI,GetWeatherInformation
from knox import views as knox_views
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('get-weather-information', GetWeatherInformation.as_view(), name='get-weather-information'),
    
]