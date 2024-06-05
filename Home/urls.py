from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('/register',views.register,name='register'),#返回注册页的视图
    path('/Home_sheller',views.Home_sheller,name='Home_sheller')#返回商家登录页的视图
]
