from django.urls import path
from . import views

urlpatterns=[
    path('a1/', views.HomeView.as_view())
]
