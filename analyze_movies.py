from __future__ import division
from collections import defaultdict
import sys
import operator


# take input argument

category = sys.argv[1]
top_number = int(sys.argv[2])

# read ratings.dat file

ratings_file = open('ratings.dat', 'r').readlines()

# length of ratings.dat

length_ratings = len(ratings_file)

# create empty list to store each column we want

ratings = [[],[],[]]

# assign each column to corresponding list
# column extracted: UserID, MovieID, Ratings

for i in range(length_ratings):

    ratings[0].append(str.split(ratings_file[i], "::")[0])
    ratings[1].append(str.split(ratings_file[i], "::")[1])
    ratings[2].append(str.split(ratings_file[i], "::")[2])

# read users.dat file

users_file = open('users.dat', 'r').readlines()

# length of users.dat

length_users = len(users_file)

# create empty list to store each column

users = [[],[],[]]

# assign each column to corresponding list
# column extracted: UserID, Gender, Age

for i in range(length_users):

    users[0].append(str.split(users_file[i], "::")[0])
    users[1].append(str.split(users_file[i], "::")[1])
    users[2].append(str.split(users_file[i], "::")[2])

# read movies.dat file

movies_file = open('movies.dat', 'r').readlines()

# length of movies.dat

length_movies = len(movies_file)

# create empty list to store each column

movies = [[],[]]

# assign each column to corresponding list
# column extracted: MovieID, Title

for i in range(length_movies):

    movies[0].append(str.split(movies_file[i], "::")[0])
    movies[1].append(str.split(movies_file[i], "::")[1])


# create dictionary for movie ID and title, this will be used for matching movie's title and ID

movie_title_dict = {}

for i in range(len(movies[0])):

    movie_title_dict[movies[0][i]] = movies[1][i]

def get_top_rated_movie(movieID, ratings, top_number):

    """
    This function will return top rated movie with given subset of data
    movieID: list of movie ID
    ratings: list of ratings corresponded to movie ID
    top_number: how many top rated movies will be returned
    """

    # create dictionaries for storing total ratings and frequency

    movie_frequency = defaultdict(int)
    movie_ratings = defaultdict(int)

    # count how many ratings each movie received and sum of ratings for each movie

    for i in range(len(movieID)):

        movie_frequency[movieID[i]] +=1

        movie_ratings[movieID[i]] += int(ratings[i])

    # calculate the average ratings for each movie

    for key in movie_ratings:

        movie_ratings[key] = movie_ratings[key]/movie_frequency[key]

    # replace the movie ID with movie title

    for key in list(movie_ratings.keys()):

        movie_ratings[movie_title_dict[key]] = movie_ratings.pop(key)

    # sort movies by average rating

    sorted_movies = sorted(movie_ratings.items(), key=operator.itemgetter(1), reverse=True)

    # return the top movies required

    return sorted_movies[:top_number]

if category == "gender":

    for i in range(length_ratings):

        # replace userID with their gender in the 'ratings' data

        ratings[0][i] = users[1][int(ratings[0][i])-1]

    # creating index for each gender's ratings

    male_index = [i for i,x in enumerate(ratings[0]) if x == "M"]
    female_index = [i for i,x in enumerate(ratings[0]) if x == "F"]

    # movies rated by male and female respectively

    male_movies = [ratings[1][x] for x in male_index]
    female_movies = [ratings[1][x] for x in female_index]

    # ratings rated by male and female respectively

    male_ratings = [ratings[2][x] for x in male_index]
    female_ratings = [ratings[2][x] for x in female_index]

    # find the top rated movies by male and female respectively

    top_movies_male = get_top_rated_movie(male_movies, male_ratings, top_number)
    top_movies_female = get_top_rated_movie(female_movies, female_ratings, top_number)

    print "gender group male: "
    print top_movies_male
    print "gender group female: "
    print top_movies_female

elif category == "agegroup":

    for i in range(length_ratings):

        # replace userID with their gender in the 'ratings' data

        ratings[0][i] = users[2][int(ratings[0][i])-1]

    # create index list for different age group

    age_group = ["1","18","25","35","45","50","56"]

    # creating empty lists for storing information for each age group

    age_index = [[] for i in range(7)]
    age_movies = [[] for i in range(7)]
    age_ratings = [[] for i in range(7)]
    age_top_movies = [[] for i in range(7)]

    for i in range(7):

        # creating index for each age group's ratings

        age_index[i] = [j for j, x in enumerate(ratings[0]) if x == age_group[i]]

        # movies rated by different age group

        age_movies[i] = [ratings[1][x] for x in age_index[i]]

        # ratings rated by different age group

        age_ratings[i] = [ratings[2][x] for x in age_index[i]]

        # find the top rated movies by different age group

        age_top_movies[i] = get_top_rated_movie(age_movies[i], age_ratings[i], top_number)

        print "age group " + age_group[i] + ": "
        print age_top_movies[i]

else:

    raise AssertionError, "please enter a valid category, choose from 'gender' and 'agegroup'"

















