from django.shortcuts import render
from .models import News
# import matplotlib.pyplot as plt
# import matplotlib
# import io
# import urllib, base64


# Create your views here.
def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss':newss})

# def statistics_view(request):
#     matplotlib.use('Agg')
#     all_movies = Movie.objects.all()
    
#     movie_counts_by_year = {}
    
#     for movie in all_movies:
#         year = movie.year if movie.year else 'None'
#         if year in movie_counts_by_year:
#             movie_counts_by_year[year] += 1
#         else:
#             movie_counts_by_year[year] = 1
            
#     bar_width = 0.5
#     bar_positions = range(len(movie_counts_by_year))
    
#     plt.bar(bar_positions, movie_counts_by_year.values(), bar_width, align='center')
    
#     plt.title('Movies per year')
#     plt.xlabel('Year')
#     plt.ylabel('Number of movies')
#     plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    
#     plt.subplots_adjust(bottom=0.3)
    
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     plt.close()
    
#     image_png = buffer.getvalue()
#     buffer.close()
#     graphic = base64.b64encode(image_png)
#     graphic = graphic.decode('utf-8')
    
#     return render(request, 'statistics.html', {'graphic':graphic})
