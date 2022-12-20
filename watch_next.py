import spacy
nlp = spacy.load('en_core_web_md')

planet_hulk = "Planet Hulk"
planet_hulk_desc = """Will he save their world or destroy it?
When the Holk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

# Define a function. In a real program, I would get the user to input the movie title and description within the function.
def Recommend_Movie(movie_title, movie_description):

    movie_list = []  # Create empty list

    with open("movies.txt", "r") as movies_file:  # Each line = a film and description
        for line in movies_file:
            movie_list.append(line)  # Add each movie to the movie list
        
    compare_movie_desc = nlp(movie_description)  # Create a description to compare all the movies to

    highest_similarity = 0  # Set highest similarity score to 0
    recommended_movie = ""  # Set the recommended movie to nothing

    for movie in movie_list:  # Compare the movie to all movies in the list
        movie_split = movie.split(":")  # Split the title by ":" so the description and title are seperate
        similarity = nlp(movie_split[1]).similarity(compare_movie_desc)  # Compare the description

        if similarity > highest_similarity:  # If the similarity is higher...
            recommended_movie = movie  # Get the movie
            highest_similarity = similarity  # Get the score

    print(f'Based on the description of {movie_title}, I recommend {recommended_movie.split(":")[0]}. Here is the description:\n{recommended_movie.split(":")[1]}')

Recommend_Movie(planet_hulk, planet_hulk_desc)  # Call the function