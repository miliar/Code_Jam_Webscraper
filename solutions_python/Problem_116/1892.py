__author__ = 'Riccardo'

import sys


SIZE = 4

X = 'X'
O = 'O'
T = 'T'
EMPTY = '.'

X_WON = 'X won'
O_WON = 'O won'
DRAW = 'Draw'
NOT_COMPLETED = 'Game has not completed'


def parse_input(filename):
    with open(filename) as f:
        n_boards = int(f.readline())
        boards = []
        board = []
        for row in f:
            row = row.strip()
            if row == '' and board:
                boards.append(board)
                board = []
            else:
                board.append(row)
        if board:
            boards.append(board)
        assert len(boards) == n_boards
    return boards


def determine_status(board):
    row_s = _check_row_status(board)
    if row_s:
        return row_s
    col_s = _check_col_status(board)
    if col_s:
        return col_s
    diag_s = _check_diag_status(board)
    if diag_s:
        return diag_s
    return _check_draw(board)


def _check_row_status(board):
    for row in board:
        winner = _check_winner(row)
        if winner:
            return winner


def _check_col_status(board):
    for i in range(SIZE):
        col = ''.join([row[i] for row in board])
        winner = _check_winner(col)
        if winner:
            return winner


def _check_diag_status(board):
    diag1 = ''.join([board[i][i] for i in range(SIZE)])
    winner = _check_winner(diag1)
    if winner:
        return winner
    diag2 = ''.join([board[SIZE - 1 - i][i] for i in range(SIZE)])
    winner = _check_winner(diag2)
    if winner:
        return winner


def _check_draw(board):
    for row in board:
        if EMPTY in row:
            return NOT_COMPLETED
    return DRAW


def _check_winner(row):
    if EMPTY not in row:
        if T in row:
            if (X in row and O not in row) or (O in row and X not in row):
                return X_WON if X in row else O_WON
        elif row[0] == row[1] and row[1] == row[2] and row[2] == row[3]:
            return X_WON if row[0] == X else O_WON


def main():
    assert len(sys.argv) == 2
    filename = sys.argv[1]
    boards = parse_input(filename)
    with open(filename[:filename.rfind('.')] + '.out', 'wt') as f:
        for n in range(len(boards)):
            print('Case #{:d}: {:s}'.format(n + 1,
                                            determine_status(boards[n])),
                  file=f)


if __name__ == '__main__':
    main()