from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.adding_book_method),
    path('display_book/<int:book_id>', views.book_detail_page),
    path('add_book_to_author/<int:author_id>', views.add_book_to_author_method),

    path('author', views.authors),
    path('add_author', views.adding_author_method),
    path('display_author/<int:author_id>', views.author_detail_page),
    path('add_author_to_book/<int:book_id>', views.add_author_to_book_method),

]