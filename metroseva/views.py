from django.http import HttpResponse
from django.shortcuts import render
import random
import requests
from django.http import JsonResponse
import json



def home(request):
    if request.method == 'GET':
        startloc=request.GET['startloc']
        destination = request.GET['Destination'] 
        startloc=startloc.lower()
        destination=destination.lower()
        startloc=startloc.replace(" ","+")
        destination=destination.replace(" ","+")
        startloc=str(startloc)
        destination=str(destination)
        
        
        url=f'https://us-central1-delhimetroapi.cloudfunctions.net/route-get?from={startloc}&to={destination}'
        try:
        # Some code that may raise an exception
            result=request.get(url)
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        
        
        context={
            "startloc":startloc,
            "destination":destination,
        }
        print(startloc)
        print(destination)
        return render(request, 'index.html',context)
            
    return render(request, 'index.html')