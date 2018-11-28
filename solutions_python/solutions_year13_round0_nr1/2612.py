
class TicTacToeTomek(object):

    def __init__(self, board, players):
        self.board = board
        self.both = 'T'
        self.empty = '.'
        self.players = players

    def set_player(self, player):
        self.player = player

    def checkwin(self):
        '''
            Checks if the player has won the game
        '''
        win = self._checkrow()
        win = win or self._checkcolumn()
        win = win or self._checkdiagonal()
        return win

    def _checkrow(self):
        '''
            Checks the rows for win
        '''
        for row in self._get_rows():
            if set(row) == set([self.player]) or set(row) == set([self.player, self.both]):
                return True
        return False

    def _checkcolumn(self):
        '''
            Checks the columns for win
        '''
#        for j in range(len(self.board)):
#            column = set([self.board[i][j] for i in xrange(len(self.board))])
        for column in self._get_columns():
            if  set(column) == set([self.player]) or set(column) == set([self.player, self.both]):
                return True
        return False

    def _checkdiagonal(self):
        '''
            Checks the diagonals for win
        '''
#        forward_diagonal = set([self.board[i][i] for i in xrange(len(self.board))])
#        reverse_diagonal = set([self.board[i][len(self.board) - 1 - i] for i in xrange(len(self.board))])
#
#        if forward_diagonal == set([self.player]) or forward_diagonal == set([self.player, self.both]):
#            return True
#        if reverse_diagonal == set([self.player]) or reverse_diagonal == set([self.player, self.both]):
#            return True
        for diagonal in self._get_diagonals():
            if set(diagonal) == set([self.player]) or set(diagonal) == set([self.player, self.both]):
                return True

        return False

    def _get_rows(self):
        '''
            Yields each row of the board
        '''
        for row in self.board:
            yield row

    def _get_columns(self):
        '''
            Yields the colunms
        '''
        for j in xrange(len(self.board)):
            yield [self.board[i][j] for i in xrange(len(self.board))]

    def _get_diagonals(self):
        '''
            Yields the diagonals. Reverse first. Forward Second
        '''
        yield [self.board[i][len(self.board) - 1 - i] for i in xrange(len(self.board))]
        yield [self.board[i][i] for i in xrange(len(self.board))]

    def check_incomplete_game(self):
        '''
            Returns True if the board shows incomplete game.
        '''
        for row in self.board:
            if row.count(self.empty) >= 1:
                return True

        for col in self._get_columns():
            if col.count(self.empty) >= 1:
                return True

        for diagonal in self._get_diagonals():
            if diagonal.count(self.empty) >= 1:
                return True

    def status(self):
        '''
            Returns the status based on the calculated status
        '''
        for player in self.players:
            self.set_player(player)
            if self.checkwin():
                return "%s won" % player

        if self.check_incomplete_game():
            return "Game has not completed"
        else:
            return "Draw"

with open("A-large.in") as f, open("tic.ot.large", "w") as out:
    num_boards = int(f.readline())

    boards = []
    for each in xrange(num_boards):
        a_board = []
        a_board.append([x for x in f.readline().rstrip()])
        a_board.append([x for x in f.readline().rstrip()])
        a_board.append([x for x in f.readline().rstrip()])
        a_board.append([x for x in f.readline().rstrip()])

        boards.append(a_board)
        f.readline()

    for i, each in enumerate(boards):
        t = TicTacToeTomek(each, ['X', 'O'])
        status = t.status()
        out.write("Case #%s: %s\n" % (i+1, status))

#if __name__ == "__main__":
#    board = [
#            ['x', 'o', 'x', 't'],
#            ['x', 'x', 'o', 'o'],
#            ['o', 'x', 'o', 'x'],
#            ['x', 'x', 'o', 'o']
#            ]
#
#    t = TicTacToeTomek(board, ['x', 'o'])
#    print t.status()
