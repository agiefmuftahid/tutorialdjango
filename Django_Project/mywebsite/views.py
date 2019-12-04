from django.shortcuts import render

def index(request):
    context = {
        'judul': 'Home',
        'subjudul':'Ini adalah halaman Home',
        'kontributor': 'Agief Muftahid',
        'img' : 'img/banner_home.png',
        'nav': [
            ['/', 'Home'],
            ['/blog','Blog'],
            ['/about','About']
        ]
    }
    return render(request,"index.html",context)