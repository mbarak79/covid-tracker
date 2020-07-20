from django.shortcuts import render
import requests
import json

# Create your views here.


def home(request):

    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"France"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    data = response['response']

    d = data[0]

    context = {
        'all': d['cases']['total'],
        'recovered': d['cases']['recovered'],
        'deaths': d['deaths']['total'],
        'new': d['cases']['new'],
        'critical': d['cases']['critical']

    }

    return render(request, 'home.html', context)

