import sys


class Prob1(object):
    def __init__(self, board):
        self.board = board
        self.output = "Draw"  # by default is a draw, so we check the rest

    def solve(self):
        if self.row() or self.column() or self.diagonal() or self.game_over():
            return self.output
        else:
            return "Draw"

    def column(self):
        for i in xrange(4):
            X, O = 0, 0
            for j in xrange(4):
                if self.board[i + 4*j] == 'X':
                    X += 1
                elif self.board[i + 4*j] == 'O':
                    O += 1
                elif self.board[i + 4*j] == 'T':
                    X += 1
                    O += 1
                else:
                    break
            if X == 4:
                self.output = "X won"
                return True
            if O == 4:
                self.output = "O won"
                return True
        return False

    def row(self):
        for i in xrange(4):
            X, O = 0, 0
            for j in xrange(4):
                if self.board[4*i + j] == 'X':
                    X += 1
                elif self.board[4*i + j] == 'O':
                    O += 1
                elif self.board[4*i + j] == 'T':
                    X += 1
                    O += 1
                else:
                    break
            if X == 4:
                self.output = "X won"
                return True
            if O == 4:
                self.output = "O won"
                return True
        return False

    def diagonal(self):

        # to the right
        X, O = 0, 0
        for i in xrange(4):
            if self.board[5*i] == 'X':
                X += 1
            elif self.board[5*i] == 'O':
                O += 1
            elif self.board[5*i] == 'T':
                X += 1
                O += 1
            else:
                break
        if X == 4:
            self.output = "X won"
            return True
        if O == 4:
            self.output = "O won"
            return True

        # to the left
        X, O = 0, 0
        for i in xrange(4):
            if self.board[3 + 3*i] == 'X':
                X += 1
            elif self.board[3 + 3*i] == 'O':
                O += 1
            elif self.board[3 + 3*i] == 'T':
                X += 1
                O += 1
            else:
                break
        if X == 4:
            self.output = "X won"
            return True
        if O == 4:
            self.output = "O won"
            return True
        return False

    def game_over(self):
        if '.' in board:
            self.output = "Game has not completed"
            return True
        return False

    @staticmethod
    def read_board(f):
        board = []
        for i in xrange(4):
            line = f.readline()
            board.extend(line.strip())
        f.readline()
        return board


output = "Case #%d: %s"

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for counter in xrange(T):
        board = Prob1.read_board(f)
        p1 = Prob1(board)
        print output % (counter+1, p1.solve())
