from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul': 'About',
        'subjudul':'Ini adalah halaman About',
        'kontributor': 'Agief Muftahid',
        'img': 'about/img/banner_about.png',
        'app_css': 'about/css/style.css',
        'nav': [
            ['/', 'Home'],
            ['/blog','Blog'],
            ['/about','About']
        ]
    }
    return render(request,'about/index.html',context)