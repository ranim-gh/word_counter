from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.template import Library


dic={"name":'Ranim' , "age": 20 }

# Create your views here.

def say_hello(request):
    dic={"name":'Ranim' , "age": 20 }

    age = 20  # Set the age variable to 20
    return  render(request , "index.html")


def counter(request):
        words= request.GET["text"]
        length = len(words.split())


        return render(request, 'counter.html', {'nigga' : length} )





