from django.http import HttpResponse
import datetime
from product.models import *
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Hello! its my project")


def goodby(request):
    return HttpResponse("Goodby user!")


def nowdate(request):
    return HttpResponse(datetime.datetime.now())


def main_view(request):
    return render(request, "layouts/index.html")


def products_view(request):
    if request.method == "GET":
        product = Product.objects.all()
        context = {
            'product': product
        }
    return render(request, 'product/product.html', context=context)
