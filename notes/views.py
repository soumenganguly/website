from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, Template, loader

# Create your views here.

def index(request):
    template = loader.get_template("notes/index.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def blog(request):
    template = loader.get_template("notes/blog.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def pictures(request):
    template = loader.get_template("notes/pictures.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def contact(request):
    template = loader.get_template("notes/contact.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def research(request):
    template = loader.get_template("notes/research.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def publications(request):
    template = loader.get_template("notes/publications.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def project(request):
    template = loader.get_template("notes/projects.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def essays(request):
    template = loader.get_template("notes/essays.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def diaries(request):
    template = loader.get_template("notes/diaries.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def how_tos(request):
    template = loader.get_template("notes/how-tos.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def poems(request):
    template = loader.get_template("notes/poems.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def trips(request):
    template = loader.get_template("notes/trips.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def random(request):
    template = loader.get_template("notes/random.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))

