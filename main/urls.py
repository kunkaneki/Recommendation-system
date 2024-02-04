from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginUser,name="login"),
    path('data', views.predict),
    path('visualization', views.visual),
    path('description', views.description),
    path('logout',views.logoutUser,name="logout"),
]
