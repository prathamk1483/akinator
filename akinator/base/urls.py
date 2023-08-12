from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('themes/',views.themes,name='themes'),
    path('cgame/',views.chara ,name='chargame'),
    path('playgame/',views.playgame ,name='playgame'),
    # path('playgame2/',views.playgame2 ,name='playgame2'),










    path('ogame/',views.obj,name='objgame'),
    path('agame/',views.ani,name='anigame'),
]
