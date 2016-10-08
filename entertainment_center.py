import fresh_tomatoes
import media

friday = media.Movie("Friday",
                        "The funniest movie of all time",
                        "http://upload.wikimedia.org/wikipedia/en/2/27/Fridayposter1995.jpg",
                        "https://www.youtube.com/watch?v=umvFBoLOOgo")
pulp_fiction = media.Movie("Pulp Fiction",
                     "A 1994 American neo-noir crime black comedy film written and directed by Quentin Tarantino,",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pulp_Fiction_%281994%29_poster.jpg/220px-Pulp_Fiction_%281994%29_poster.jpg",
                     "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
harlem_nights = media.Movie("Harlem Nights",
                        "A 1989 American black comedy crime film written, executive produced, and directed by Eddie Murphy. ",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/b/b5/Harlem-nights-poster-1.jpg/220px-Harlem-nights-poster-1.jpg",
                        "https://www.youtube.com/watch?v=En27DgNW0nY")
training_day = media.Movie("Training Day",
                        "A 2001 American neo-noir crime thriller film directed by Antoine Fuqua, written by David Ayer, and starring Denzel Washington and Ethan Hawke",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/b/b3/Training_Day_Poster.jpg/220px-Training_Day_Poster.jpg",
                        "https://www.youtube.com/watch?v=DXPJqRtkDP0")
baby_boy = media.Movie("Baby Boy",
                     "This film follows bicycle mechanic Joseph (Jody) Summers as he lives and learns in his everyday life in the hood.",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/3/36/Baby_boy.jpg/220px-Baby_boy.jpg",
                     "https://www.youtube.com/watch?v=vhe9MZi-lHk")
brown_sugar = media.Movie("Brown Sugar",
                        "The film is a story of lifelong friends, A&R Andre and Editor-in-Chief Sidney. The two can attribute their friendship and the launch of their careers to a single, seminal childhood moment - the day they discovered hip-hop.",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/4/40/Brown_sugar_poster.jpg/220px-Brown_sugar_poster.jpg",
                        "https://www.youtube.com/watch?v=FGjaZBuciC8")

movies = [friday, pulp_fiction, harlem_nights, training_day, baby_boy, brown_sugar]
#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
