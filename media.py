class Video(object):
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url =  trailer_youtube_url

class Movie(Video):
    """Class to describe data and methods for movies"""
    def __init__(self, title, poster_image_url, trailer_youtube_url,
                 release_year):
        super(Movie, self).__init__(title, poster_image_url,
                                    trailer_youtube_url)
        self.release_year = release_year


class Show(Video):
    """Class to describe data and methods for TV shows"""
    def __init__(self, title, poster_image_url, trailer_youtube_url,
                 number_of_seasons):
        super(Show, self).__init__(title, poster_image_url,
                                    trailer_youtube_url)
        self.number_of_seasons = number_of_seasons
