import webbrowser

class Movie:
    """ Class to define the movie class """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open_new_tab(self.trailer_url)