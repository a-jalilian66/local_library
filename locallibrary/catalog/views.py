from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    num_books = models.Book.objects.count()
    num_instances = models.BookInstance.objects.count()
    num_instances_available = models.BookInstance.objects.filter(status__exact='a').count()
    num_authors = models.Author.objects.count()

    return render(
        request,
        'catalog/index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors}
    )
