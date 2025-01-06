from django.shortcuts import render # type: ignore

# Create your views here.
def welcome(response):
    return render(response, 'welcome.html')