from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
import datetime

def index_p(request):
    template_name = 'test_app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('index_PAGE'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)
def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    filepath = '/'
    file_list = str(os.listdir(filepath))
    return HttpResponse(file_list)


# Create your views here.
