from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

from .models import Movie

# Create your views here.

def home(request):
    # return HttpResponse('<h1>Welcome to Home Page</h1>')
    # return render(request, 'home.html')
    # return render(request, 'home.html', {'name':'Simon Villa Escobar'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:        
        movies = Movie.objects.all()
    return render(request, 'home.html', {'movies':movies, 'searchTerm':searchTerm})
    

def about(request):
    # return HttpResponse('<h1>Welcome to About Page</h1>')
    return render(request, 'about.html')

# Username: simon
# Email: test@email.com
# Pw: test
import matplotlib.pyplot as plt
import io
import base64
from collections import defaultdict
import movie  # Asegúrate de importar tu modelo Movie correctamente

def statistics_view(request):
    matplotlib.use('Agg')
    all_movies = Movie.objects.all()
    
    movie_counts_by_year = {}
    movie_counts_by_genre = defaultdict(int)  # Usamos defaultdict para contar los géneros
    
    for movie in all_movies:
        year = movie.year if movie.year else 'None'
        if year in movie_counts_by_year:
            movie_counts_by_year[year] += 1
        else:
            movie_counts_by_year[year] = 1
            
        # Contar películas por género
        if movie.genre:  # Asumiendo que "genre" es el campo que contiene los géneros de la película
            first_genre = movie.genre.split(',')[0]  # Obtenemos el primer género
            movie_counts_by_genre[first_genre] += 1
    
    # Gráfico de barras de películas por año
    bar_width = 0.5
    bar_positions_year = range(len(movie_counts_by_year))
    
    plt.bar(bar_positions_year, movie_counts_by_year.values(), bar_width, align='center')
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions_year, movie_counts_by_year.keys(), rotation=90)
    
    plt.subplots_adjust(bottom=0.3)
    
    buffer_year = io.BytesIO()
    plt.savefig(buffer_year, format='png')
    buffer_year.seek(0)
    plt.close()
    
    image_png_year = buffer_year.getvalue()
    buffer_year.close()
    graphic_year = base64.b64encode(image_png_year)
    graphic_year = graphic_year.decode('utf-8')
    
    # Gráfico de barras de películas por género
    genre = list(movie_counts_by_genre.keys())
    counts = list(movie_counts_by_genre.values())
    
    plt.bar(genre, counts)
    plt.title('Movies per genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies')
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.3)
    
    buffer_genre = io.BytesIO()
    plt.savefig(buffer_genre, format='png')
    buffer_genre.seek(0)
    plt.close()
    
    image_png_genre = buffer_genre.getvalue()
    buffer_genre.close()
    graphic_genre = base64.b64encode(image_png_genre)
    graphic_genre = graphic_genre.decode('utf-8')
    
    return render(request, 'statistics.html', {'graphic_year': graphic_year, 'graphic_genre': graphic_genre})

