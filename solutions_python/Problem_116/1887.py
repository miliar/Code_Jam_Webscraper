import sys


GAME_NOT_COMPLETE = 'Game has not completed'
GAME_DRAW = 'Draw'
GAME_X_WON = 'X won'
GAME_O_WON = 'O won'


def row_result(values):
    """
    Returns the result of the given values string:
    0: tie
    1: X wins
    2: 0 wins
    """
    if '.' in values:
        return 0
    x_row = values.replace('T', 'X')
    if x_row == 'XXXX':
        return 1
    o_row = values.replace('T', 'O')
    if o_row == 'OOOO':
        return 2
    return 0


class GameBoard:
    ROWS = (
        (0, 1, 2, 3),
        (4, 5, 6, 7),
        (8, 9, 10, 11),
        (12, 13, 14, 15),
        (0, 4, 8, 12),
        (1, 5, 9, 13),
        (2, 6, 10, 14),
        (3, 7, 11, 15),
        (0, 5, 10, 15),
        (3, 6, 9, 12)
    )

    def __init__(self, case_number, board_state):
        self.case_number = case_number
        self.empty_spaces = 0
        self.cells = []
        for x in board_state.replace('\n', ''):
            if x == '.':
                self.empty_spaces += 1
            self.cells.append(x)

    def __str__(self):
        return 'Case #%i: %s' % (self.case_number, self.result())

    def result(self):
        for row in self.ROWS:
            row_val = ''
            for position in row:
                row_val += self.cells[position]
            result = row_result(row_val)
            if result == 1:
                return GAME_X_WON
            if result == 2:
                return GAME_O_WON
        if not self.empty_spaces:
            return GAME_DRAW
        return GAME_NOT_COMPLETE


if __name__ == '__main__':
    #assert row_result('.XOO') == 0
    #assert row_result('XXXX') == 1
    #assert row_result('TXXX') == 1
    #assert row_result('OOOO') == 2
    #assert row_result('TOOO') == 2

    #test_cases = (
        #'XXXT....OO......',
        #'XOXTXXOOOXOXXXOO',
        #'XOX.OX..........',
        #'OOXXOXXXOX.TO..O',
        #'XXXO..O..O..T...',
        #'OXXXXO....O....O'
    #)

    #for index, test_case in enumerate(test_cases):
        #print GameBoard(index, test_case)

    num_cases = None
    current_case = 1
    board_state = ''
    for line in sys.stdin:
        if not num_cases:
            num_cases = line
            continue
        if line == '\n':
            print GameBoard(current_case, board_state)
            board_state = ''
            current_case += 1
        else:
            board_state += line
