from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre
from django.views import generic

# Create your views here.

def index(request):
    num_books = Book.objects.all().count
    num_instances = BookInstance.objects.all().count

    num_instances_availible = BookInstance.objects.filter(status='a').count()

    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_availible': num_instances_availible,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'

class BookDetailView(generic.DetailView):
    model = Book