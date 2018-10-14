import sys

class board():
    def __init__(self, matrix):
        self.matrix = matrix

    def get_row(self, n):
        return self.matrix[n]

    def get_col(self, n):
        return [self.matrix[i][n] for i in xrange(4)]

    def get_diagonal(self, n):
        if n==0:
            return [self.matrix[i][i] for i in xrange(4)]
        return [self.matrix[i][3-i] for i in xrange(4)]

    def __str__(self):
        ret = ""
        for i in range(4):
            for j in range(4):
                ret += self.matrix[i][j]
            ret += '\n'
        return ret

# Reads 4 lines and a newline, returns board
def read_board():
    matrix = [['' for i in xrange(4)] for i in xrange(4)]
    for i in xrange(4):
        row = f.readline()
        for j in xrange(4):
            matrix[i][j] = row[j]
    throwaway = f.readline()
    return board(matrix)

# returns the proper string for the gamestate of a board
def get_gamestate(b):
    # returns None if indecisive, otherwise decided string from 4-cell
    def fourcell(r):
        all_x = None
        all_o = None
        for i in range(4):
            if r[i] == 'X' or r[i] == 'T':
                if r[i] == 'X': all_o = False
                if all_x is None: all_x = True
            if r[i] == 'O' or r[i] == 'T':
                if r[i] == 'O': all_x = False
                if all_o is None: all_o = True
            if r[i] == '.':
                all_x = all_o = False
        if all_x: return "X won"
        if all_o: return "O won"

    # returns true if the board is full, false otherwise
    def is_finished(b):
        for i in range(4):
            for j in range(4):
                if b.matrix[i][j] == '.': return False
        return True

    for i in range(4):
        if i<=1:
            r = fourcell(b.get_diagonal(i))
            if r is not None: return r
        r = fourcell(b.get_row(i))
        if r is not None: return r
        r = fourcell(b.get_col(i))
        if r is not None: return r

    if is_finished(b): return "Draw"
    return "Game has not completed"


f = open(sys.argv[1], 'r')

T = int(f.readline())

boards = [read_board() for i in range(T)]

to_write = ''

case = 1
for b in boards:
    to_write += "Case #"+str(case)+": "+get_gamestate(b)
    if case != T:
        to_write += '\n'
    case += 1

o = open(sys.argv[1]+'_output', 'w')
o.write(to_write)
