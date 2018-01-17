from django.http import HttpResponse
import datetime
# from django.template.context_processors import request

def hello(request):
    return HttpResponse("Hello world\n this is hello page")

def my_homepage_view(request):
    return HttpResponse("this is home page \n welcome to here")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> It is now %s.\n %s</body></html>" % (now,hello(request))
    return HttpResponse(html)