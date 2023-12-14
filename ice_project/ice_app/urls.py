
from django.urls import path
from . import views
#name space declre
app_name='ice_app'

urlpatterns = [

    path('',views.index,name='index'),
    path('ice/<int:ice_id>/',views.detail,name='detail'),
    path('add/',views.add_icecream,name='add_icecream'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

]