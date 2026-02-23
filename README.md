# MovieVerse 🎬
Deprecated no longer viable


## ✨ Features

- **Modern UI/UX**: Responsive design with modern animations and transitions
- **Real-time Search**: Instant search results as you type
- **Movie Details**: Comprehensive movie information including:
  - Cast and crew
  - Ratings and reviews
  - Similar movie recommendations
  - Release dates and runtime
- **Trending Movies**: Weekly updated trending movies section
- **Top Rated**: Collection of highest-rated movies
- **Responsive Design**: Fully responsive on all devices

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- TMDB API key (get it from [TMDB website](https://www.themoviedb.org/documentation/api))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/movieverse.git
cd movieverse
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your TMDB API key:
```env
TMDB_API_KEY=your_api_key_here
```

5. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📁 Project Structure

```
movieverse/
│
├── app.py                  # Main Flask application file
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables
│
├── static/                # Static files
│   ├── css/              # Custom CSS files
│   └── js/               # JavaScript files
│
└── templates/            # HTML templates
    ├── index.html        # Home page template
    └── movie.html        # Movie details template
```

## 🔧 Configuration

The application uses the following environment variables:

- `TMDB_API_KEY`: Your TMDB API key
- `FLASK_ENV`: Set to `development` for debug mode
- `FLASK_APP`: Set to `app.py`

## 🛠️ Built With

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [TMDB API](https://www.themoviedb.org/documentation/api) - Movie data
- [TailwindCSS](https://tailwindcss.com/) - Styling
- [Alpine.js](https://alpinejs.dev/) - JavaScript framework

## 📝 API Routes

### Main Routes

- `GET /`: Home page with trending and top-rated movies
- `GET /movie/<movie_id>`: Detailed view of a specific movie
- `GET /search`: Search endpoint for real-time movie search

### API Response Format

Search endpoint returns JSON in the following format:
```json
{
  "results": [
    {
      "id": "movie_id",
      "title": "Movie Title",
      "release_date": "YYYY-MM-DD",
      "poster_path": "/path/to/poster",
      "vote_average": 8.5
    }
  ]
}
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for providing the movie data API
- [Flask Documentation](https://flask.palletsprojects.com/) for the excellent web framework
- [TailwindCSS](https://tailwindcss.com/) for the utility-first CSS framework

## 📧 Contact

jasperfernandezvegas@gmail.com

STATUS: DEPRECATED 

