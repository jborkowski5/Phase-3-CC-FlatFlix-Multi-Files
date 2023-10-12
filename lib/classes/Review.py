class Review:

    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        self.movie._reviews.append(self)
        self.movie._viewers.append(self.viewer)

        self.viewer._reviews.append(self)
        self.viewer._movies.append(self.movie)

        Review.all.append(self)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if not hasattr(self, "_rating"):
            if isinstance(rating, int) and 1 <= rating <= 5:
                self._rating = rating
            else:
                raise Exception("rating cannot be changed after it is set")
        else:
            raise Exception("rating cannot be changed after it is set")

    @property 
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, viewer):
        from classes.Viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("Invalid viewer")

    @property 
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie):
        from classes.Movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("Invalid movie")            