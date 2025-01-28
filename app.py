# app.py
from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# Configure TMDB API settings
TMDB_API_KEY = 'baaf3d6292cfbc3e74b83553527d3423'  # Replace with your actual API key
TMDB_BASE_URL = 'https://api.themoviedb.org/3'
TMDB_IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'

def fetch_movie_data(endpoint, params=None):
    """Helper function to fetch data from TMDB API"""
    default_params = {'api_key': TMDB_API_KEY, 'language': 'en-US'}
    if params:
        default_params.update(params)
    
    response = requests.get(f'{TMDB_BASE_URL}/{endpoint}', params=default_params)
    return response.json()

@app.route('/')
def index():
    # Fetch trending movies
    trending = fetch_movie_data('trending/movie/week')
    # Fetch top rated movies
    top_rated = fetch_movie_data('movie/top_rated')
    
    return render_template('index.html', 
                         trending=trending['results'][:8],
                         top_rated=top_rated['results'][:8],
                         image_base_url=TMDB_IMAGE_BASE_URL)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    if query:
        results = fetch_movie_data('search/movie', {'query': query})
        return jsonify(results)
    return jsonify({'results': []})

@app.route('/movie/<movie_id>')
def movie_detail(movie_id):
    movie = fetch_movie_data(f'movie/{movie_id}')
    credits = fetch_movie_data(f'movie/{movie_id}/credits')
    similar = fetch_movie_data(f'movie/{movie_id}/similar')
    
    return render_template('movie.html',
                         movie=movie,
                         credits=credits,
                         similar=similar['results'][:6],
                         image_base_url=TMDB_IMAGE_BASE_URL)

if __name__ == '__main__':
    app.run(debug=True)
