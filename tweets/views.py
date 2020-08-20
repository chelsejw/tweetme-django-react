from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from tweets.models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello world!!</h1>")
0
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    print(args, kwargs)
    status = 200
    data = {
        "id": tweet_id,
    }
    try:
        tweet = Tweet.objects.get(id=tweet_id)
        data['content'] = tweet.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)
