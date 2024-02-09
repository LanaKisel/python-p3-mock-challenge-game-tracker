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
        self._username = username 
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(self.username) <= 16:          
            self._username = username
        else:
            raise Exception('username must be a string between 2 and 16 characters long')    


    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        games = []
        for result in self.results():
            games.append(result.game)
        return games    

    def played_game(self, game):
        for result in self.results():
            if result.game == game:
                return True
            else:
                return False

    def num_times_played(self, game):
        count = 0
        if self.played_game(game):
            count +=1
        return count    

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



