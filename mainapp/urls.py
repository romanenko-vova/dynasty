from django.urls import path

from mainapp.views import main, family

app_name = 'mainapp'

urlpatterns = [
    path('', main),
    path('gariny/', family, name='family')
]
