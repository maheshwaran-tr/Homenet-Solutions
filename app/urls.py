from django.urls import path
from . import views

urlpatterns = [
    path("test/",views.testing,name="home"),
    path("getall/",views.getCategory,name="getall"),
    path('add/',views.add_student,name="add")
]