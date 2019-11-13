from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Account

class ShowIndex(TemplateView):
    template_name = 'index.html'


class ShowAllSavings(ListView):
    model = Account
    template_name = 'showids.html'
    queryset = Account.objects.filter(type='savings')


class ShowDetails(DetailView):
    model = Account
    template_name = 'show.html'


class DisplayAllcurrent(ListView):
    model = Account
    template_name = 'displayids.html'
    queryset = Account.objects.filter(type='current')

class DisplayDetails(DetailView):
    model = Account
    template_name = 'display.html'
