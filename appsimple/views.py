from django.shortcuts import render
from .models import Name, NameForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
     """ """
     form = NameForm()
     context_instance = RequestContext(request)
     return render_to_response('home.html',{'form':form},context_instance)


