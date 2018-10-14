import sys
import pdb

class Reader:
    def __init__(self, filename):
        self.fp = open(filename)

    def read(self):
        tokens = self.fp.readline().split()
        result = []
        for token in tokens:
            try:
                result.append(int(token, 10))
            except ValueError:
                result.append(token)
        return result

    def read_strings(self):
        tokens = self.fp.readline().split()
        return tokens

def bits(x, n):
    result = []
    for i in xrange(n - 1, -1, -1):
        result.append((x & (1 << i)) != 0)
    return result

class Board:
    def __init__(self, board):
        self.board = board
        self.row_count = len(board)
        self.col_count = len(board[0])
        assert all(len(row) == self.col_count for row in board)
        self.opt = [[None] * self.col_count for i in xrange(self.row_count)]
        
    def remove_largest_square(self):
        for i in xrange(self.row_count):
            self.opt[i][0] = 1 if self.board[i][0] is not None else 0
        for j in xrange(self.col_count):
            self.opt[0][j] = 1 if self.board[0][j] is not None else 0
        for i in xrange(1, self.row_count):
            for j in xrange(1, self.col_count):
                here = self.board[i][j]
                up = self.board[i - 1][j]
                left = self.board[i][j - 1]
                upleft = self.board[i - 1][j - 1]
                if here is None:        # burned out
                    self.opt[i][j] = 0
                elif (here is upleft is True and up is left is False) or \
                   (here is upleft is False and up is left is True):
                    self.opt[i][j] = min(self.opt[i - 1][j - 1],
                                         self.opt[i][j - 1],
                                         self.opt[i - 1][j]) + 1
                    assert self.opt[i][j] >= 2
                else:
                    self.opt[i][j] = 1
        square_max = 0
        square_i = square_j = None
        for i in xrange(self.row_count):
            for j in xrange(self.col_count):
                if self.opt[i][j] > square_max:
                    square_max = self.opt[i][j]
                    square_i, square_j = i, j

        # return if no square to remove
        if square_i is None:
            return 0

        # burn out the removed square
        for i in xrange(square_i - square_max + 1, square_i + 1):
            for j in xrange(square_j - square_max + 1, square_j + 1):
                self.board[i][j] = None

        # return the size of the largest square
        return square_max

    def tiles_left(self):
        return sum(sum(x is not None for x in row) for row in self.board)

    def dump(self):
        tiles = {None: 'X', True: '@', False: '.'}
        for row in self.board:
            print ''.join(tiles[x] for x in row)

if __name__ == '__main__':
    reader = Reader(sys.argv[1])
    case_count, = reader.read()
    for case in xrange(case_count):
        # dynamic programming woo
        row_count, col_count = reader.read()
        board = []
        for i in xrange(row_count):
            row_hex, = reader.read_strings()
            board.append(bits(int(row_hex, 16), col_count))
        board = Board(board)
        square_counts = {}
        while True:
            size = board.remove_largest_square()
            if size == 0:
                break
            elif size == 1:
                square_counts.setdefault(1, 0)
                square_counts[1] += 1
                square_counts[1] += board.tiles_left()
                break
            else:
                square_counts.setdefault(size, 0)
                square_counts[size] += 1
        assert sum(size**2 * count for size, count in
            square_counts.iteritems()) == row_count * col_count
        print "Case #%d: %d" % (case + 1, len(square_counts))
        for size in reversed(square_counts.keys()):
            print "%d %d" % (size, square_counts[size])
