from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'judul': 'Blog',
        'subjudul':'Ini adalah halaman Blog',
        'kontributor': 'Agief Muftahid',
        'img' : 'blog/img/banner_blog.png',
        'app_css': 'blog/css/style.css',
        'nav': [
            ['/', 'Home'],
            ['/blog','Blog'],
            ['/about','About']
        ]
    }
    return render(request, 'blog/index.html', context)


def news(request):
    context = {
        'judul': 'News',
        'kontributor': 'Agief Muftahid',
        'nav': [
            ['/', 'Home'],
            ['/blog','Blog'],
            ['/blog/news','News'],
            ['/about','About']
        ]
    }
    return render(request, 'index.html', context)

def cerita(request):
    context = {
        'judul': 'Cerita',
        'kontributor' : 'Agief Muftahid'
    }
    return render(request, 'index.html', context)

def recent(request):
    return HttpResponse('<h1>Ini adalah recent post!</h1>') 