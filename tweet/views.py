from django.shortcuts import render
from .models import Tweet
from .forms import Tweetform , UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, "index.html")

def tweet_list(requset):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(requset, "tweet_list.html", {"tweets": tweets})

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = Tweetform(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = Tweetform()
    return render(request, "tweet_form.html", {"form": form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = Tweetform(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect("tweet_list")
    else:
        form = Tweetform(instance=tweet)
    return render(request, "tweet_form.html", {"form": form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweet_confirm_delete.html", {"tweet": tweet})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tweet_list')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

def tweet_list(request):
    query = request.GET.get("q")
    if query:
        tweets = Tweet.objects.filter(text__icontains=query)
    else:
        tweets = Tweet.objects.all()
    return render(request, "tweet_list.html", {"tweets": tweets})

