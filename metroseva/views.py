from django.http import HttpResponse
from django.shortcuts import render
import random
import requests
from django.http import JsonResponse
import json



def home(request):
    if request.method == 'POST':
        startloc=request.POST['startloc']
        destination = request.POST['Destination'] 
        
        s=startloc
        d=destination
        startloc=startloc.lower()
        destination=destination.lower()
        startloc=startloc.replace(" ","+")
        destination=destination.replace(" ","+")
        startloc=str(startloc)
        destination=str(destination)
        
        url=f"https://us-central1-delhimetroapi.cloudfunctions.net/route-get?from={startloc}&to={destination}"
        # Some code that may raise an exception
        response = requests.get(url)
        data = response.json()
        interchanges=data['interchange']
            
        number_of_interchanges=len(interchanges)
        
        
        context={
            "startloc":s,
            "destination":d,
            "interchanges":interchanges,
            "number_of_interchanges":number_of_interchanges,
        }
        print(startloc)
        print(destination)
        return render(request, 'index.html',context)
            
    return render(request, 'index.html')

def results(request):
    return render(request, 'route.html')