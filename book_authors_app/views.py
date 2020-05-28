from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, 'index.html', context)
    
def adding_book_method(request):
    Book.objects.create(title=request.POST["title"], desc=request.POST["description"])
    return redirect("/")

def book_detail_page(request, book_id):
    context = {
        "one_book": Book.objects.get(id=book_id),
        'all_authors': Author.objects.all()

    }
    return render(request, 'display_book.html', context)

def authors(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)
    

def adding_author_method(request):
    Author.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], notes=request.POST["notes"]), 
    return redirect("/author")

def author_detail_page(request, author_id):
    context = {
        "one_author": Author.objects.get(id=author_id),
        'all_books': Book.objects.all()
    }
    return render(request, 'display_author.html', context)

def add_author_to_book_method(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_author = Author.objects.get(id=request.POST["author"])
    this_author.books.add(this_book)
    return redirect(f'/display_book/{book_id}')

def add_book_to_author_method(request, author_id):
    this_author = Author.objects.get(id=author_id)
    this_book = Book.objects.get(id=request.POST["book"])
    this_book.authors.add(this_author)
    return redirect(f'/display_author/{author_id}')

