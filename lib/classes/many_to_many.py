class Game:
    all = []
    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title") and len(title):
            self._title = title
        else:
            raise Exception('title should be a not empty string')    

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        players = []
        for result in self.results():
            players.append(result.player)    
        return players    

    def average_score(self, player):
        count = 0
        sum_score = 0
        for result in self.results():
            count +=1
            sum_score += result.score
        average = sum_score / count
        if count >0:
            return average
        else:
            return 0    
        pass

class Player:
    all = []
    def __init__(self, username):
        self.username = username 
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:          
            self._username = username
        else:
            raise Exception('username must be a string between 2 and 16 characters long')    

    def results(self):
        return [result for result in Result.all if result.player == self]
   
    def games_played(self):
        return list({result.game for result in self.results()})    

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        games= []
        for result in self.results():
            games.append(result.game)
        return games.count(game)

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.score = score
        self.game = game     
        Result.all.append(self)      

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, 'score') and 1<= score <= 5000:
            self._score = score
        else:
            raise Exception("score must be int between 1 and 5000")    
    
    @property 
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if type(player)== Player:
            self._player = player    
        else:
            raise Exception('player must be a typr of Player')
    
    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if type(game) == Game:
            self._game = game 
        else:
            raise Exception("game must be a type of Game")       



# from statistics import mean
# class Game:
#     all = []

#     def __init__(self, title):
#         self.title = title
#         type(self).all.append(self)

#     @property
#     def title(self):
#         return self._title

#     @title.setter
#     def title(self, title):
#         if isinstance(title, str) and not hasattr(self, "title") and title:
#             self._title = title
#         else:
#             raise Exception

#     def results(self):
#         return [result for result in Result.all if result.game is self]

#     def players(self):
#         return list({result.player for result in self.results()})

#     def average_score(self, player):
#         scores = [result.score for result in player.results() if result.game is self]
#         return mean(scores) if len(scores) else 0



# class Player:
#     all = []

#     def __init__(self, username):
#         self.username = username
#         type(self).all.append(self)

#     @property
#     def username(self):
#         return self._username

#     @username.setter
#     def username(self, username):
#         if isinstance(username, str) and 2 <= len(username) <= 16:
#             self._username = username
#         else:
#             raise Exception

#     def results(self):
#         return [result for result in Result.all if result.player is self]

#     def games_played(self):
#         return list({result.game for result in self.results()})

#     def played_game(self, game):
#         return game in self.games_played()

#     def num_times_played(self, game):
#         games_played = [result.game for result in self.results()]
#         return games_played.count(game)

#     @classmethod
#     def highest_scored(cls, game):
#         averages = [(game.average_score(player), player) for player in cls.all]
#         if not averages:
#             return None
#         highest_record_tuple = max(averages, key=lambda tup: tup[0])
#         return highest_record_tuple[1]

# class Result:
#     all = []

#     def __init__(self, player, game, score):
#         self.player = player
#         self.game = game
#         self._score = score
#         type(self).all.append(self)

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, score):
#         if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000:
#             self._score = score
#         else:
#             raise Exception

#     @property
#     def player(self):
#         return self._player

#     @player.setter
#     def player(self, player):
#         if isinstance(player, Player):
#             self._player = player
#         else:
#             raise Exception

#     @property
#     def game(self):
#         return self._game

#     @game.setter
#     def game(self, game):
#         if isinstance(game, Game):
#             self._game = game
#         else:
#             raise Exception