from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('/register',views.register,name='register')#返回注册页的视图
]
