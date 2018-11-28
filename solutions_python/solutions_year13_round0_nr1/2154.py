mapping = {
    '.' : 0,
    'X' : 1,
    'O' : -1,
    'T' : 2,
    0 : '.',
    1 : 'X',
    -1 : 'O',
    2 : 'T'
}

class Board:

    def __init__(self, input=None):
        if not input:
            self.board = [[0 for i in range(4)] for j in range(4)]
        else:
            self.board = []
            for line in input:
                row = [mapping[c] for c in line.strip()]
                self.board.append(row)
            assert(len(self.board) == 4)

    def __str__(self):
        display_board = [[mapping[i] for i in row] for row in self.board]
        output_strings = [''.join(row) for row in display_board]
        return '\n'.join(output_strings)

    @property
    def rows(self):
        return self.board

    @property
    def columns(self):
        return [[self.board[i][j] for i in range(0,4)] for j in range(0,4)]

    @property
    def diagonals(self):
        tl_br = [self.board[i][i] for i in range(0,4)]
        bl_tr = [self.board[i][3-i] for i in range(0,4)]
        return [tl_br, bl_tr]

    def evaluate(self):

        def evaluate_line(line, player):
            if line.count(mapping[player]) == 3 and line.count(mapping['T']) == 1:
                return True
            if line.count(mapping[player]) == 4:
                return True
            return False

        for line in (self.rows + self.columns + self.diagonals):
            if evaluate_line(line, 'X'):
                return 'X won'
            if evaluate_line(line, 'O'):
                return 'O won'

        for line in self.rows:
            if 0 in line:
                return 'Game has not completed'

        return 'Draw'

if __name__ == '__main__':
    import sys

    if sys.argv[1:]:
        filename = sys.argv[1]
    else:
        exit('Usage: %s <input_file>' % sys.argv[0])
    
    cases = []
    with open(filename) as f:
        data = f.readlines()
        num_cases = int(data[0])
        for start_index in range(1, len(data), 5):
            raw_board_strings = data[start_index:start_index + 4]
            board_strings = [row.strip() for row in raw_board_strings]
            board = Board(input=board_strings)
            cases.append(board)

    # for i,c in enumerate(cases):
    #     print 'Case #%s: %s' % (i+1, c.evaluate())
    fout = filename.replace('.in', '.out')
    with open(fout, 'wb') as f:
        for i,c in enumerate(cases):
            f.write('Case #%s: %s\n' % (i+1, c.evaluate()))
