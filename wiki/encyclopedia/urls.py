from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.get_page, name="wiki"),
    path("search/", views.searchpage, name="searchpage"),
    path("search/title", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("edit/<str:title>/", views.edit, name="edit"),
    path("random/", views.get_random, name="random"),
]