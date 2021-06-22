from django.shortcuts import render ,HttpResponse,redirect
from markdown2 import Markdown
from . import util
from .forms import title,post
from django.contrib import messages
from django.urls import reverse
import random

def index(request):
    context={
                "entries": util.list_entries()
    }
    return render(request, "encyclopedia/index.html", context)

def get_page(request,title):
    entry=util.get_entry(title)
    context={
        "title":title,
        "entry":entry
    }
    return render(request, "encyclopedia/EntryPage.html",context)
    
def search(request):
    if request.method == 'POST':
        form = title(request.POST or None)
        if request.method == "POST" and form.is_valid():
            t=form.cleaned_data['title']
            entries= util.list_entries()
            res = [i for i in entries if t in i] 
            print(res)
            if len(res) !=0:
                context={
                "entries":res
                }
                return render(request, "encyclopedia/index.html", context)
            else:
                messages.info(request,' Title doesnot exist. ')
                return render(request, "encyclopedia/fail.html")
        else:
            return render(request, "encyclopedia/index.html")

def create(request):
    if request.method == 'POST':
        form = post(request.POST or None)
        if form.is_valid():
            t=form.cleaned_data['title']
            c=form.cleaned_data['content']
            entries= util.list_entries()
            if t in entries:
                context={
                    "t":t
                }
                return render(request, "encyclopedia/exist.html",context)
            else:
                save=util.save_entry(t,c)
                context={
                "entries": util.list_entries()
                }
                return render(request, "encyclopedia/index.html",context)
        else:
            messages.warning(request,'Enter both the fields ')
            return render(request, "encyclopedia/fail.html")
    else:
        return render(request, "encyclopedia/create.html")

def edit(request,title):
    if request.method == 'POST':
        form = post(request.POST or None)
        if  form.is_valid():
            t=form.cleaned_data['title']
            c=form.cleaned_data['content']
            save=util.save_entry(t,c)
            return redirect(reverse('index'))
        else:
            messages.warning(request,'Enter both the fields ')
            return render(request, "encyclopedia/fail.html")
    else:
        entry=util.get_entry(title)
        context={
            'title':title,
            'entry':entry,
        }
        return render(request, "encyclopedia/editpage.html",context)

def get_random(request):
    entries= util.list_entries()
    title=random.choice(entries)
    entry=util.get_entry(title)
    context={
        "title":title,
        "entry":entry
    }
    return render(request, "encyclopedia/EntryPage.html",context)

def searchpage(request):
    return render(request, "encyclopedia/search.html")

