class Board:

    def __init__(self, moves):
        """
        Initializes the Board class with an input of 4 by 4 integer array
        that describe the moves of two players
        """
        self.moves = moves

    def state(self):
        """
        () -> string

        Describes the state of the game:
        X won, O won, draw, or not completed
        """
        winner = self.get_winner()
        has_empty = self.check_empty()

        if (winner):
            return winner + ' won'
        else:
            return (has_empty and 'Game has not completed') or 'Draw'

    def get_winner(self):
        """
        () -> String

        Returns the winner of the current move.
        If there's a winner, returns that winner.
        Otherwise, empty string '' (equivalent to `False') will be returned
        """
        # check all rows
        for row in range(4):
            s = self.line_state(lambda arr, x: arr[row][x])
            if (s):
                return s

        # check all cols
        for col in range(4):
            s = self.line_state(lambda arr, x: arr[x][col])
            if (s):
                return s

        # check left diag
        s = self.line_state(lambda arr, x: arr[x][x])
        if (s):
            return s

        # check right diag
        s = self.line_state(lambda arr, x: arr[x][3 - x])
        if (s):
            return s
    
    def line_state(self, fn):
        """
        (fn) -> string

        Describes the state of the specified line:
        X won, O won, draw or contains empty

        precondition: each symbol in the line have to be one of
        'X', 'O', 'T' or '.'

        returns: 'X' if x won; 'O' if o won; empty string if no one won
        """
        x_count = 0
        o_count = 0
        has_t = False
        for i in range(4):
            cell = fn(self.moves, i)
            if (cell == '.'):
                return '' # if there's empty cell, no one won
            if (cell == 'X'):
                x_count += 1
            elif (cell == 'O'):
                o_count += 1
            else:
                has_t = True
        if (x_count == 4):
            return 'X'
        if (o_count == 4):
            return 'O'
        if (has_t):
            if (x_count == 3):
                return 'X'
            if (o_count == 3):
                return 'O'
        return ''

    def check_empty(self):
        """
        () -> Boolean

        Checks whether there are empty cells in the current move
        """
        for row in range(4):
            for col in range(4):
                if (self.moves[row][col] == '.'):
                    return True

if __name__ == '__main__':
    import sys
    try:
        fname = sys.argv[1]
        try:
            fin = open(fname)
            case_count = fin.readline()
            for c in range(int(case_count)):
                moves = [['' for x in range(4)] for x in range(4)]
                for i in range(4):
                    row = fin.readline()
                    for j in range(4):
                        moves[i][j] = row[j]
                fin.readline() # skip empty lines
                board = Board(moves)
                print "Case #" + str(c + 1) + ":", board.state()
        except IOError:
            print "File", fname, "does not exist."
    except IndexError:
        print "Please specify name of the input file."
