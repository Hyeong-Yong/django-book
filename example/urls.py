from django.urls import path, include
from rest_framework import routers
from .views import helloAPI, bookAPI, booksAPI, BookAPI, BooksAPI, BookViewSet #BooksAPIMixins, BookAPIMixins

router = routers.SimpleRouter()
router.register('books', BookViewSet)
urlpatterns = [
    path("hello/", helloAPI),
    # function
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
    # class
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
    # class + mixins or class + generics
    # path("mixin/books/", BooksAPIMixins.as_view()),
    # path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),
    
]

urlpatterns = router.urls