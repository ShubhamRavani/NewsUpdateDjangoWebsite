from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

# Create your views here.


def index(request):
    import requests
    import json

    news_api_request = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&apiKey=416d40d6b6c6459599569c89fdc6e146")

    api = json.loads(news_api_request.content)

    return render(request, 'news/index.html', {'api': api})


def contact(request):
    return render(request, 'news/contact.html')


def business(request):
    import requests
    import json

    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=416d40d6b6c6459599569c89fdc6e146")
    api = json.loads(news_api_request.content)

    return render(request, 'news/business.html', {'api': api})


def entertainment(request):
    import requests
    import json

    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=416d40d6b6c6459599569c89fdc6e146")
    api = json.loads(news_api_request.content)

    return render(request, 'news/entertainment.html', {'api': api})


def health(request):
    import requests
    import json

    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=416d40d6b6c6459599569c89fdc6e146")
    api = json.loads(news_api_request.content)

    return render(request, 'news/health.html', {'api': api})


def science(request):
    import requests
    import json

    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=416d40d6b6c6459599569c89fdc6e146")
    api = json.loads(news_api_request.content)

    return render(request, 'news/science.html', {'api': api})


def sports(request):
    import requests
    import json

    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=416d40d6b6c6459599569c89fdc6e146")
    api = json.loads(news_api_request.content)

    return render(request, 'news/sports.html', {'api': api})


def technology(request):
    import requests
    import json

    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=416d40d6b6c6459599569c89fdc6e146")
    api = json.loads(news_api_request.content)

    return render(request, 'news/technology.html', {'api': api})
