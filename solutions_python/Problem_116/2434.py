
from numpy import matrix


class TicTacToeTomek(object):

    def __init__(self, board):
        self.board = matrix(board)

    def get_result(self):
        for item_list in self.get_lists():
            if self.check_list(item_list, 'X'):
                return 'X won'
            elif self.check_list(item_list, 'O'):
                return 'O won'

        if '.' in self.board:
            return 'Game has not completed'

        return 'Draw'

    def get_lists(self):
        # Lines
        lists = self.board.tolist()

        # Columns
        lists += self.board.T.tolist()

        # Diagonals
        i = range(4)
        j = i[::-1]
        # Main diagonal
        lists.append(self.board[i, i].tolist()[0])
        # Anti diagonal
        lists.append(self.board[i, j].tolist()[0])

        return lists

    def check_list(self, item_list, player):
        if item_list.count(player) == 4:
            return player
        if item_list.count(player) == 3 and 'T' in item_list:
            return player
        return None


file_input = open('1.input')
file_output = open('1.output', 'a+')

number_tests = int(file_input.readline())

for case in xrange(1, number_tests + 1):
    matrix_game = []
    for line in xrange(4):
        matrix_game.append(list(file_input.readline().strip()))

    game = TicTacToeTomek(matrix_game)
    file_output.write("Case #{0}: {1}".format(case, game.get_result()))
    # if not last read empty line and break line
    if case < number_tests:
        file_input.readline()
        file_output.write("\n")
