#   0123
# 0 ....
# 1 ....
# 2 ....
# 3 ....

class Game:
    def __init__(self, size = 4):
        self.size = 4
        self.rows = { 'X': 0, 'O': 0 }
        self.columns = {}
        self.columns['X'] = [True] * size
        self.columns['O'] = [True] * size
        self.diagonals = {'X': [True, True], 'O': [True, True]}
        self.empty = 0
        self.result = None

    def add_empty(self):
        self.empty += 1

    def add_to_row(self, symbol):
        self.rows[symbol] += 1

    def discard_diagonal(self, symbol, i, j):
        if i == j:
            self.diagonals[symbol][0] = False
        if (self.size - i - 1) == j:
            self.diagonals[symbol][1] = False

    def discard_column(self, symbol, column):
        self.columns[symbol][column] = False

    def discard_row(self, symbol):
        self.rows[symbol] = 0

    def check_and_clean_rows(self):
        for symbol in self.rows.keys():
            if self.rows[symbol] == self.size:
                self.result = symbol
            self.rows[symbol] = 0

    def game_over(self):
        if not self.result:
            for symbol in self.columns.keys():
                if any(self.columns[symbol]):
                    self.result = symbol
                    break
            for symbol in self.diagonals.keys():
                if any(self.diagonals[symbol]):
                    self.result = symbol
                    break
            if not self.result:
                if self.empty:
                    self.result = 'N'
                else:
                    self.result = 'D'

    def print_result(self, game_count):
        if self.result in ('X', 'O'):
            print "Case #%i: %s won" % (game_count, self.result)
        elif self.result == 'D':
            print "Case #%i: Draw" % (game_count)
        elif self.result == 'N':
            print "Case #%i: Game has not completed" % (game_count)

def get_stats(input):
    n = int(input.readline().strip())

    counts = {}

    other = { 'X': 'O', 'O': 'X' }

    g = Game()
    game_count = 1
    i = 0
    j = 0
    while game_count <= n:
        line = input.readline().strip()
        i = 0
        for cell in line:
            if cell == 'T':
                g.add_to_row('X')
                g.add_to_row('O')
            elif cell == '.':
                g.discard_column('X', i)
                g.discard_column('O', i)
                g.discard_diagonal('X', i, j)
                g.discard_diagonal('O', i, j)
                g.add_empty()
            elif cell in ('X', 'O'):
                g.add_to_row(cell)
                g.discard_row(other[cell])
                g.discard_column(other[cell], i)
                g.discard_diagonal(other[cell], i, j)
            i += 1

        g.check_and_clean_rows()
        j += 1
        if j >= g.size:
            g.game_over()

        if g.result:
            g.print_result(game_count)
            if i == 0: input.readline()
            while input.readline().strip(): pass
            g = Game()
            game_count += 1
            i = 0
            j = 0


if __name__ == '__main__':
    import sys
    get_stats(sys.stdin)
