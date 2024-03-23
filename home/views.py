from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "home/index.html", context)

# Create your views here.
