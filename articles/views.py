from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from .forms import ArticleForm
def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles_list.html', {'articles': articles})

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles_list')
        else:
            form = ArticleForm()
    return render(request, 'articles/create_article.html', {'form': form})

