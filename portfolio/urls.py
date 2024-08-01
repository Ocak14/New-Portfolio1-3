from django.urls import path
from .views import index_view, books_view, PortfolioListView, About_view, Gallery_view, blog_view, ContactFormView, Portfolio_Single_view,Gallery_Single_view

from . import views
urlpatterns = [
    path('', index_view, name='index-page'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    path('books/', books_view, name='books-page'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio-page'),
    path('about/', About_view, name='about-page'),
    path('gallery/', Gallery_view, name='gallery-page'),
    path('blog/', blog_view, name='blog-page'),
    path('portfolio-single/', Portfolio_Single_view, name='portfolio-single-page'),
    path('gallery_single/', Gallery_Single_view,name='gallery-single-page')
]
