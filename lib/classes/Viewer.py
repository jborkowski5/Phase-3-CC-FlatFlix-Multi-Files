class Viewer:

    all = []

    def __init__(self, username):
        self.username = username
        self._movies = []
        self._reviews = []
        Viewer.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if type(username) == str and 6 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Invalid username")
        
    def reviews(self):
        return self._reviews

    def reviewed_movies(self):
        return list(set(self._movies))

    def has_reviewed_movie(self, movie):
        return any(review.movie == movie for review in self._reviews)

    def add_review(self, movie, rating):
        from classes.Review import Review
        review = Review(self, movie, rating)
        return review