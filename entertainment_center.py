import fresh_tomatoes
import media

do_the_right_thing = media.Movie("Do The Right Thing",
                                 "Racial tension during on of the hottest days of summer",
                                 "https://upload.wikimedia.org/wikipedia/en/2/22/DO_THE_RIGHT_THING.jpg",
                                 "https://youtu.be/6xXnQwLZzB0")

star_wars = media.Movie("Star Wars",
                        "The Rebel Alliance works to destroy the Galactic Empire's Death Star",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://youtu.be/vP_1T4ilm8M")

love_jones = media.Movie("Love Jones",
                         "Get together, Fall apart, Fall back in love",
                         "https://upload.wikimedia.org/wikipedia/en/2/2c/LoveJonesMovie.jpg",
                         "https://youtu.be/xNMoQ_Cqt4E")

malcolm_x = media.Movie("Malcolm X",
                        "The Drama version of the life of Malcolm X",
                        "https://upload.wikimedia.org/wikipedia/en/4/49/Malcolmxdvdset.jpg",
                        "https://youtu.be/sx4sEvhYeVE")

brown_sugar = media.Movie("Brown Sugar",
                          "Story of two friends who love Hip Hop and each other",
                          "https://upload.wikimedia.org/wikipedia/en/4/40/Brown_sugar_poster.jpg",
                          "https://youtu.be/1cMkcfL8w5k")

the_notebook = media.Movie("The Notebook",
                           "A story of a young couple who falls in love in the 40s",
                           "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",
                           "https://youtu.be/S3G3fILPQAU")

movies = [do_the_right_thing, love_jones, star_wars, malcolm_x, brown_sugar, the_notebook]
fresh_tomatoes.open_movies_page(movies)