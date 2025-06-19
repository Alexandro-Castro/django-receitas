from django.urls import path
from core.views import home, about, test_base

urlpatterns = [
    path('', home),
    path('about/',about),
    path('base', test_base)
]
