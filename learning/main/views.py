from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Проверка работы</h1>")


def about(request):
    return HttpResponse("<h1>Страница про нас</h1>")


def lena(request):
    return HttpResponse("<h1>Скоро тут будет Лена</h1>")