from django.urls import path

from.views import index, contato, export, soma, inicio

urlpatterns = [
    path('', index),
    path('contato', contato),
    path('export', export),
    path('soma', soma),
    path('inicio', inicio),

]

