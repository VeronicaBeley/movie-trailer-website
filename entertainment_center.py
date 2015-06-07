
import fresh_tomatoes
import media

ironman = media.Movie("Iron Man"
                   ,"After being held captive in an Afghan cave, an industrialist creates a unique weaponized suit of armor to fight evil."
                   ,"http://www.movieartarena.com/imgs/ironman1int.jpg"
                   ,"www.youtube.com/watch?v=8hYlB38asDY")



hulk = media.Movie("The Incredible Hulk"
                    ,"Bruce Banner, a scientist on the run from the U.S. Government must find a cure for the monster he emerges whenever he loses his temper. However, Banner then must fight a soldier whom unleashes himself as a threat stronger than he."
                    ,"http://www.freemovieposters.net/posters/incredible_hulk_the_2008_351_poster.jpg"
                    ,"www.youtube.com/watch?v=KNbPnqyvItk")



ironman2 = media.Movie("Iron Man 2"
                    ,"After being held captive in an Afghan cave, an industrialist creates a unique weaponized suit of armor to fight evil."
                    ,"http://www.wired.com/images_blogs/underwire/2010/03/iron_man_poster_1200.jpg"
                    ,"https://www.youtube.com/watch?v=QUD106HC7uA")

thor = media.Movie("Thor"
                    ,"The powerful but arrogant god Thor is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders."
                    ,"http://vignette2.wikia.nocookie.net/marvelcinematicuniverse/images/5/5a/Thor_Official_Poster.jpg/revision/20121220212003"
                    ,"www.youtube.com/watch?v=eOrNdBpGMv8")

captainamerica = media.Movie("Captain America: The First Avenger"
                    ,"Steve Rogers, a rejected military soldier transforms into Captain America after taking a dose of a Super-Soldier serum. But being Captain America comes at a price as he attempts to take down a war monger and a terrorist organization."
                    ,"http://itcouldabeenbetter.com/wp-content/uploads/2013/12/Captain-America-The-First-Avenger.jpg"
                    ,"www.youtube.com/watch?v=KNbPnqyvItk")

avengers = media.Movie("The Avengers"
                    ,"When Thor's evil brother, Loki, gains access to the unlimited power of the energy cube called the Tesseract."
                    ,"http://www.theaterhopper.com/wordpress/wp-content/uploads/2012/02/avengers_poster.jpg"
                    ,"www.youtube.com/watch?v=eOrNdBpGMv8")






movies = [ironman, hulk, ironman2, thor, captainamerica, avengers]
fresh_tomatoes.open_movies_page(movies)




