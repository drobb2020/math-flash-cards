from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('addition/', views.addition, name="addition"),
    path('subtraction/', views.subtraction, name="subtraction"),
    path('multiplication/', views.multiplication, name="multiplication"),
    path('division/', views.division, name="division"),
]
