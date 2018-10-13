__author__ = 'Christian Hersevoort'

number_of_games = None
tttt_boards = []

class TicTacToeTomek:
    _board = []

    def __init__(self, board_lines):
        self._board = [['?' for x in xrange(4)] for x in xrange(4)]
        self.setup_board(board_lines)

    def setup_board(self, board_lines):
        if len(board_lines) != 4:
            raise Exception("Invalid board size")

        for y, line in enumerate(board_lines):
            for x, char in enumerate(line):
                self._board[y][x] = char

    def has_winner_row(self, row, who):
        return ((self._board[row][0] is who or self._board[row][0] is 'T') and
                (self._board[row][1] is who or self._board[row][1] is 'T') and
                (self._board[row][2] is who or self._board[row][2] is 'T') and
                (self._board[row][3] is who or self._board[row][3] is 'T')
        )

    def has_winner_column(self, column, who):
        return ((self._board[0][column] is who or self._board[0][column] is 'T') and
                (self._board[1][column] is who or self._board[1][column] is 'T') and
                (self._board[2][column] is who or self._board[2][column] is 'T') and
                (self._board[3][column] is who or self._board[3][column] is 'T')
        )

    def has_winner_diagonal_top_left(self, who):
        return ((self._board[0][0] is who or self._board[0][0] is 'T') and
                (self._board[1][1] is who or self._board[1][1] is 'T') and
                (self._board[2][2] is who or self._board[2][2] is 'T') and
                (self._board[3][3] is who or self._board[3][3] is 'T')
        )

    def has_winner_diagonal_top_right(self, who):
        return ((self._board[0][3] is who or self._board[0][3] is 'T') and
                (self._board[1][2] is who or self._board[1][2] is 'T') and
                (self._board[2][1] is who or self._board[2][1] is 'T') and
                (self._board[3][0] is who or self._board[3][0] is 'T')
        )

    def has_open_spot(self):
        for line in self._board:
            for char in line:
                if char is '.':
                    return  True
        return False

    def get_output_result(self):
        for player in ['X', 'O']:
            for xy in range(0, 4):
                if self.has_winner_row(xy, player):
                    return "%s won" % player
                if self.has_winner_column(xy, player):
                    return "%s won" % player
                if self.has_winner_diagonal_top_left(player):
                    return "%s won" % player
                if self.has_winner_diagonal_top_right(player):
                    return "%s won" % player

        if self.has_open_spot():
            return "Game has not completed"
        else:
            return "Draw"

    def __repr__(self):
        result = ''
        for line in self._board:
            for char in line:
                result += char
            result += '\n'
        return result

def read_input():
    global number_of_games
    global tttt_boards

    with open('problem-a/input.txt') as fp:
        number_of_games = int(fp.readline())
        for n in range(0, number_of_games):
            board = []
            for m in range(0, 4):
                board.append(fp.readline().strip('\n'))

            tttt_boards.append(TicTacToeTomek(board))
            #read empty 'split' line
            fp.readline()

if __name__ == "__main__":
    read_input()
    fp = open('out-file.out', 'w')
    for case in range(0, number_of_games):
        result =  "Case #%d: %s\n" % (case + 1, tttt_boards[case].get_output_result())
        fp.write(result)
