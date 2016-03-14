'''The media module contains classes for various types of video media'''

class Video(object):
    '''Parent for all video-related media items

    Attributes:
        title (str): The name of the video
        poster_image_url (str): A url for the video's cover art
        trailer_youtube_url (str): A url for the video's trailer on youtube
    '''
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

class Movie(Video):
    '''Class to describe data and methods for movies

    Attributes:
        title (str): The name of the video
        poster_image_url (str): A url for the video's cover art
        trailer_youtube_url (str): A url for the video's trailer on youtube
        release_year (int): The year the movie was released
    '''
    def __init__(self, title, poster_image_url, trailer_youtube_url,
                 release_year):
        super(Movie, self).__init__(title, poster_image_url,
                                    trailer_youtube_url)
        self.release_year = release_year

    def output_specific_content(self):
        '''Returns content specific to movies, e.g., release years'''
        return self.release_year


class Show(Video):
    '''Class to describe data and methods for TV shows

    Attributes:
        title (str): The name of the video
        poster_image_url (str): A url for the video's cover art
        trailer_youtube_url (str): A url for the video's trailer on youtube
        number_of_seasons (int): The number of seasons the show has released
    '''
    def __init__(self, title, poster_image_url, trailer_youtube_url,
                 number_of_seasons):
        super(Show, self).__init__(title, poster_image_url,
                                    trailer_youtube_url)
        self.number_of_seasons = number_of_seasons

    def output_specific_content(self):
        '''Returns content specific to TV shows, e.g., number of seasons'''
        content = str(self.number_of_seasons) + " Season" + (
                                # Output plural as appropriate
                                "s" if self.number_of_seasons > 1 else ""
                            )
        return content
