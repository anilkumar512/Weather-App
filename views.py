import requests
from django.shortcuts import redirect, render
from .models import Weather
# Create your views here.
def search(request):
    city=request.GET.get('q','')
    context={'city':city}
    if city :
        URL=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3558832005761a9148ad56b0533702b7'
        resp=requests.get(url=URL)
        if resp.status_code==200:
            data=resp.json()
            context['data']=data
            context['temperature']=round(data['main']['temp']-273.15,2)
        else:
            context['data']=None
            context['error']='City Not Found or API error'


    return render(request,'search.html',context)