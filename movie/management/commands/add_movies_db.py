from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load from movie_description.json into the Movie model'
    
    def handle(self, *args, **kwargs):
        # Construct the full path to the JSON file
        json_file_path = 'movie/management/commands/movies.json'
        
        # Load data from the JSON file
        with open(json_file_path, 'r') as file:
            movies = json.load(file)
            
        # Add products to the database
        for i in range(100):
            movie = movies[i]
            exist = Movie.objects.filter(title=movie['title']).first() # Check if the movie already exists
            if not exist:
                Movie.objects.create(title = movie['title'],
                                     image = 'movie/images/Default.jpg',
                                     genre = movie['genre'],
                                    year = movie['year'])
                
                    