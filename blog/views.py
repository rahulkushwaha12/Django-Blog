from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from . import models
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
#from django.shortcuts import render_to_response
#from contacts.models import ContactForm
#from django.template import RequestContext, Context
#from django import forms
#from django.forms.widgets import *
#from django.core.mail import send_mail, BadHeaderError

class BlogIndex(generic.ListView):
	queryset = models.Entry.objects.published()
	randomArticle = models.Entry.objects.published().order_by('?')
	template_name = "home.html"
	paginate_by = 10

class BlogDetail(generic.DetailView):
	model = models.Entry
	template_name = "post.html"

def about(request):
	return render_to_response('about.html',context_instance=RequestContext(request))
def calender(request):
	return render_to_response('opc-calender.html',context_instance=RequestContext(request))
def forum(request):
	return render_to_response('forum.html',context_instance=RequestContext(request))
def search(request):
	return render_to_response('search.html',context_instance=RequestContext(request))

#def contactview(request):

#		subject = request.POST.get('topic', '')
#		from_email = request.POST.get('email', '')
#
#		if subject and message and from_email:
#		        try:
#					send_mail(subject, message, from_email, ['change@this.com'])
 #       		except BadHeaderError:
  #          			return HttpResponse('Invalid header found.')
   #     		return HttpResponseRedirect('/contact/thankyou/')
	#	else:
	#		return render_to_response('contacts.html', {'form': ContactForm()})
	#
	#	return render_to_response('contacts.html', {'form': ContactForm()},
	#		RequestContext(request))

#def thankyou(request):
#		return render_to_response('thankyou.html')