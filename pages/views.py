from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    x=2
    y=3
    return HttpResponse("Hello, world!")

def hello(request):
    return render(request, 'hello.html',{"name":"Aryan"})
