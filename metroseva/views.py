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
        path=data['path']
        time=data['time']
        time=int(time)
        change=[]
        
        for j in range(len(interchanges)):
            name="line"+str(j+1)
            val=data[name]
            val[0]=val[0]+" to "
            change.append(val)
            
        
        towards=[]
        towards_data=data['lineEnds']
        for i in range(len(towards_data)):
            towards.append(towards_data[i])
        
            
        number_of_interchanges=len(interchanges)
        
        
        context={
            "startloc":s,
            "destination":d,
            "interchanges":interchanges,
            "number_of_interchanges":number_of_interchanges,
            "path":path,
            "time":time,
            "change":change,
            "towards":towards,
        }
        print(startloc)
        print(destination)
        return render(request, 'index.html',context)
            
    return render(request, 'index.html')

def results(request):
    return render(request, 'route.html')