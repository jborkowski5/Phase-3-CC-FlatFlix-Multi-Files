class Movie:

    all = []

    def __init__(self, title):
        self.title = title
        self._viewers = []
        self._reviews = []
        Movie.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception("must be str over 0 characters")    

    def reviews(self):
        return self._reviews

    def reviewers(self):
        return list(set(self._viewers))

    def average_rating(self):
        if not self._reviews:
            return None
        total_ratings = sum(review.rating for review in self._reviews)
        average = round(total_ratings / len(self._reviews), 1)
        return average
    
    @classmethod
    def highest_rated(cls):
        if not cls.all:
            return None 

        highest_rated_movie = None
        highest_average_rating = 0 

        for movie in cls.all:
            average = movie.average_rating()
            if average is not None and average > highest_average_rating:
                highest_average_rating = average
                highest_rated_movie = movie

        return highest_rated_movie