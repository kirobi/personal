from wow.models import book
from django.shortcuts import render_to_response
from django.template import RequestContext
def home(request):
    info= book.objects.all()

    return render_to_response('index.html',context_instance=RequestContext(request,locals()))