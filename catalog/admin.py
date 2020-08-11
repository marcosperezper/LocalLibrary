from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

class BookInLine(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    #Mostrar los campos en forma de lista
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #Mostrar los campos de fecha juntos en una linea
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines =  [BookInLine]

admin.site.register(Author,AuthorAdmin)

#Mostrar BookInstance en la vista de Book
class BookInstanceInline(admin.TabularInline):
    model =  BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
     #Mostrar los campos en forma de lista
     list_display = ('title', 'author', 'display_genre')
     inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
     #Mostrar los campos en forma de lista
     list_display = ('id','book','status','due_back')
     #Filtro por estado y fecha limite
     list_filter = ('status', 'due_back')
     #Separar los campos por secciones
     fieldsets = (
         (None, {
             'fields' : ('book','imprint','id')
         }),
         ('Availability', {
             'fields' : ('status','due_back')
         }),
     )