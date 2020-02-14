from django.shortcuts import render
from django.http import HttpResponse

# this acts like data we queried from our db.
posts = [
    {
        'author': 'nando',
        'title': 'bloge',
        'content': 'First post content',
        'date_posted': 'February 14, 2020'

    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'foodfight/html/home.html', context)

def about(request):
    return render(request, 'foodfight/html/about.html', {'title':'about'})
