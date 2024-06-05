from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'Home/Home.html')
    # return HttpResponse("你好")#测试请求是否可行
def register(request):
    return render(request,'Home/register.html')
def Home_sheller(request):
    return render(request,'Home/Home_sheller.html')
