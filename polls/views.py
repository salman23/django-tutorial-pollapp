from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)
    template = loader.get_template("polls/index.html")
    context = RequestContext(request, {'latest_poll_list': latest_poll_list})
    return HttpResponse(template.render(context))

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Exception:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})
