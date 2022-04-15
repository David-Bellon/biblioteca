from django.urls import path

from . import views

app_name = "bliblio"
urlpatterns = [
    path("", views.index, name="index"),
]