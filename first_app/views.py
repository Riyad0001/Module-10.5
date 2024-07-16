from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
    return HttpResponse("hiiii")

def page(request):
    lst={'name':'Riyad','age':22,'home':'dhaka','bazar':{
        'alu':'2kg',
        'beef':'1kg',
        'fish':400,
        'korola':500
    },'x':"I Like My Bile",
    'y':["I","Love","Python","so","much"],
    'a':[
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31}
],
    'Date':datetime.datetime.now(),
    'z':""
    }
    
    return render(request,'index.html',lst)
