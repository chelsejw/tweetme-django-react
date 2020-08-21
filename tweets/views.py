from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings
from django.shortcuts import render, redirect
from tweets.models import Tweet
from tweets.forms import TweetForm
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    # return HttpResponse("<h1>Hello world!!</h1>")
    return render(request, 'pages/home.html', context = {}, status=200)

def tweet_create_view(req, *args, **kwargs):
    form = TweetForm(req.POST or None)

    next_url = req.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        #can do other form related logic shere
        obj.save()
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect('/')

        form = TweetForm()
    return render(req, 'components/form.html', context = {"form": form})

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    print(qs)
    tweets = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        'response': tweets
    }
    return JsonResponse(data, status=200)

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
