# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
#from .models import 

class HomePageView(TemplateView):
    template_name ='base.html'
def home(request):
	return render(request,'index.html')



# Create your views here.

