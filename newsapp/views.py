from django.views.generic import ListView, DetailView # импортируем классы
from .models import News # Импорт  нашей модели

class NewsList(ListView):
    model = News  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML
    context_object_name = 'all_news'  # это имя списка, в котором будут лежать все объекты
    queryset = News.objects.order_by('-news_create_time')

class NewsDetail(DetailView):
    model = News  # указываем модель, объекты которой мы будем выводить/ отдельная новость
    template_name = 'news_one.html'  # указываем имя шаблона,  в котором будет лежать одна новость
    context_object_name = 'one_news'  # это имя списка, в котором будут лежать один объект