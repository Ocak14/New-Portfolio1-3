from typing import Any
from django.shortcuts import render
from .models import Contact,Gallery,Blog,Books,Portfolio,About,PortfolioCategory,Portfolio_Single,Gallery_Single
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator
from .forms import ContactForm
from django.views.generic.edit import FormView
from .bot import send_message
from django.views.generic.list import ListView

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class =ContactForm
    success_url = "/"
 
    def form_valid(self,form):
      name = form.cleaned_data.get('name')
      email = form.cleaned_data.get('email')
      content = form.cleaned_data.get('content')
      text = f"Name: {name}\nEmail: {email}\ntext: {content}"
      send_message(text)
      form.save()
      return super().form_valid(form)


def index_view(request):
 return render(request,'index.html')


def About_view(request):
    about =About.objects.all()
    context = {
       "about" :about,
    }
    return render(request,'about.html', context)





def Gallery_view(request):
    gallery = Gallery.objects.all()
    context = {
        "gallery":gallery,
    }

    return render(request, 'Gallery.html',context)


def blog_view(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs,
    }
    return render(request, 'blog.html', context)


def books_view(request):
    books = Books.objects.all()
    context = {
        "books" : books,
    }
    return render(request, 'books.html',context)

# def portfolio_view(request):
#     portfolio = Portfolio.objects.all()
#     context = {
#         "portfolio" : portfolio,
#     }
#     return render(request, 'portfolio.html', context = context)

class PortfolioListView(ListView):
    model = Portfolio
    # paginate_by = 100
    context_object_name = 'portfolios'
    template_name = "portfolio.html"



    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["categories"] = PortfolioCategory.objects.all()
        return context
    


def Portfolio_Single_view(request):
    portfolio_single = Portfolio_Single.objects.all()
    context = {
        "portfolio_single" : portfolio_single,
    }
    return render(request, 'portfolio_single.html', context)



def Gallery_Single_view(request):
   gallery = Gallery.objects.all()
   context = {
        "gallery":gallery,
    }
   return render(request, 'gallery-single.html', context)
