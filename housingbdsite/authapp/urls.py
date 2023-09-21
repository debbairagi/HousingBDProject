from django.urls import path
from authapp import views

urlpatterns = [
    path('add/', views.add_musician, name='add_musician'),
    path('', views.musician_list, name='musician_list'),
    path('add_album', views.add_album, name='add_album'),
    
]