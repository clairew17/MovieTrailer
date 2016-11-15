import fresh_tomatoes
import media

# List your favorite movies here
dr_strange = media.Movie('Dr Strange', 'dr strange intro here'\
    , 'https://cdn.amctheatres.com/titles/images/Poster/Large/3353_doctor-strange_1132.jpg'\
    , 'https://www.youtube.com/watch?v=Lt-U_t2pUHI')
fantastic_beasts = media.Movie('Fantastic Beasts And Where To Find Them', 'by David Yates'\
    , 'https://cdn.amctheatres.com/titles/images/Poster/Standard/3774_fantastic-beasts-and-where-t_8B6C.jpg'\
    , 'https://www.youtube.com/watch?v=YdgQj7xcDJo')
billy_lynn = media.Movie('Billy Lynn\'s Long Halftime Walk', 'Ang Lee'\
    , 'https://cdn.amctheatres.com/titles/images/Poster/Large/4706_billylynn_D052.jpg'\
    , 'https://www.youtube.com/watch?v=mUULFJ_I048')

medias = [dr_strange, fantastic_beasts, billy_lynn]

if __name__ == "__main__":
    fresh_tomatoes.open_movies_page(medias)
