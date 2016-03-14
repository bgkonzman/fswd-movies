import fresh_tomatoes
import media

# Instantiate movie objects
donnie_darko = media.Movie(     "Donnie Darko",
                                "http://www.standbyformindcontrol.com/wp-content/uploads/2013/02/Donnie-Darko-2002-movie-poster3.jpg", # NOQA
                                "https://www.youtube.com/watch?v=ZZyBaFYFySk",
                                2001)

cool_hand_luke = media.Movie(   "Cool Hand Luke",
                                "http://ia.media-imdb.com/images/M/MV5BODMyMDA0MTY2OF5BMl5BanBnXkFtZTcwMzkzNjk3OA@@._V1_SX640_SY720_.jpg", # NOQA
                                "https://www.youtube.com/watch?v=l3CPz21NzUc",
                                1967)

jean_brodie = media.Movie(      "The Prime of Miss Jean Brodie",
                                "http://ia.media-imdb.com/images/M/MV5BMjEwNTQ4OTA2MF5BMl5BanBnXkFtZTcwODMwNTUyMQ@@._V1_SX640_SY720_.jpg", # NOQA
                                "https://www.youtube.com/watch?v=AmNQVo1qpD8",
                                1969)

# Instantiate TV show objects
house_of_cards = media.Show(    "House of Cards",
                                "https://pmctvline2.files.wordpress.com/2015/12/cwukypqxaaazfdr.png?w=600&h=750", # NOQA
                                "https://www.youtube.com/watch?v=NTzycsqxYJ0",
                                4)

game_of_thrones = media.Show(   "Game of Thrones",
                                "http://ia.media-imdb.com/images/M/MV5BMjM5OTQ1MTY5Nl5BMl5BanBnXkFtZTgwMjM3NzMxODE@._V1_UX182_CR0,0,182,268_AL_.jpg", # NOQA
                                "https://www.youtube.com/watch?v=CuH3tJPiP-U",
                                5)

expanse = media.Show(           "The Expanse",
                                "https://lh6.googleusercontent.com/-q7i_5Ot1noE/VOZk-85YvAI/AAAAAAAAACE/sqWwWreN_8o/w1108-h1600/c09b551e-0245-43d9-b9ad-7d35b08e9482.png.watermark.png", # NOQA
                                "https://www.youtube.com/watch?v=8X5gXIQmY-E",
                                1)

# Gather the shows into lists
movie_list = [donnie_darko, cool_hand_luke, jean_brodie]
show_list = [house_of_cards, game_of_thrones, expanse]

# Create and open the trailer site
fresh_tomatoes.open_page(movie_list, show_list)
