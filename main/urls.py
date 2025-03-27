from django.urls import path

from .views import main_view, result_view

urlpatterns = [
    path('', main_view, name='main'),
    path('result/', result_view, name='result'),
]