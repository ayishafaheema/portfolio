from django.http import HttpResponse
from django.shortcuts import render


def test_function(request):
    return HttpResponse("welcome to django")
def test(request):
    return render(request, "test.html")
def portfolio(request):
    return render(request, "index.html")



# Create your views here.
