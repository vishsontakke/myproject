from django.urls import path
from .views import model_view

urlpatterns = [
    path('', model_view, name='model_view'),
]
