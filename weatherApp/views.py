from django.shortcuts import redirect, render, HttpResponse
import requests
# Create your views here.


def weather(request):
    return render(request, 'weather.html')

def check_weather(request):
    check = 'sys'
    if request.method == 'POST':
        city = request.POST['city']
        wheather = '19a0d845f6126941c5a4874af325d786'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'APPID':wheather,'q':city,'units':'imperial'}
        response = requests.get(url,params)
        wheather = response.json()
        if check in wheather:
            data = {
                'city':city.upper(),
                'country': wheather['sys']['country'].upper(),
                'description' : wheather['weather'][0]['description'].upper(),
                'forecast' : wheather['weather'][0]['main'].upper(),
                'temperature' : str(wheather['main']['temp']).upper(),
                'humidity': str(wheather['main']['humidity']).upper(),
                'icon': wheather['weather'][0]['icon'],
                'pressure': str(wheather['main']['pressure']).upper(),
                'wind': str(wheather['wind']['speed'])
            }
            
            return render(request,'weather.html',data)
        else:
            alert=True
            return render(request,'weather.html',{'alert':alert})