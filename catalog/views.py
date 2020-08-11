from django.shortcuts import render
from .models import Book,Author,BookInstance,Genre
from django.views import generic

# Create your views here.

def index(request):
    """
    Funcion vista para la pagina de inicio
    """
    #Genera contadores de algos de los objetos principales
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    #Libros disponibles (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    #Renderiza la plantilla HTML index.html con los datos de la variable contexto

    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list' 
    template_name = 'books/'

    def get_queryset(self):
        return Book.objects.filter(title__icontains='El')[:5]
    def get_context_data(self,**kwargs):
        #Call the base implementation fisrt to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        #Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context