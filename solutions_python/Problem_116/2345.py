import sys

O = 1
X = 2
T = 3

class TicTacToeTomek:
    tokens = {
        'O': O,
        'X': X,
        'T': T,
        '.': None
    }

    inv_tokens = {v:k for k, v in tokens.items()}

    def __init__(self, board_string):
        self.board = self.parse(board_string)

    def __str__(self):
        out = ""
        for row in self.board:
            for move in row:
                out += self.inv_tokens[move]
            out += '\n'
        return out

    def parse(self, board):
        game = [[],[],[],[]]
        for i, char in enumerate(board):
            row = int(i / 5)
            if char != '\n':
                game[row].append(self.tokens[char])
        return game

    def samewinner(self, a, b):
        if a == None or b == None:
            return None
        if a == b:
            return a
        if a == T:
            return b
        if b == T:
            return a

    def winner(self, seq):
        return reduce(lambda a,b: self.samewinner(a, b), seq)

    def solve(self):
        solutions = {
            None: "Draw",
            O: "O won",
            X: "X won",
            T: "Game has not completed"
        }
        rows = self.board
        columns = zip(*rows)
        diagonals = [[], []]
        diagonals[0] = [rows[i][i] for i in range(4)]
        diagonals[1] = [rows[i][3 - i] for i in range(4)]
        seqs = rows + columns + diagonals
        winner = None
        for row in seqs:
            winner = self.winner(row)
            if winner is not None:
                return solutions[winner]
        for row in self.board:
            if None in row:
                return solutions[T]
        return solutions[None]

def main():
    sys.stdin.readline()
    current_board = ""
    case = 1
    for row in sys.stdin:
        current_board += row
        if row == '\n':
            print "Case #{0}: {1}".format(case, TicTacToeTomek(current_board).solve())
            current_board = ""
            case += 1

main()
