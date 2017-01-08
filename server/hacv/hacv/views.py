from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


@require_http_methods(["GET", "POST"])
def post_status(request):
    fhandle_r = open("static/post_status.html", 'r')
    html = fhandle_r.read()
    return HttpResponse(html)
