from django.urls import path
from . import views

app_name = "listings"

urlpatterns = [
    path('', views.index, name='index'),
    path('listings', views.all_listings, name='listings'),
    path('new_listing/', views.new_listing, name='new_listing'),
]
