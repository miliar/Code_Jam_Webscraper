from collections import Counter


SIZE = 4


def read_board():
    board = []
    for i in xrange(SIZE):
        row = raw_input()
        board.append(row)
    raw_input()
    return board


def is_finished(board):
    for row in board:
        if '.' in Counter(row):
            return False
    return True


def check_row(row):
    counts = Counter(row)
    for player in ['X', 'O']:
        if counts[player] == 4 or (counts[player] == 3 and
                                   counts['T'] == 1):
            return player
    return None


def check_rows(board):
    for row in board:
        result = check_row(row)
        if result:
            return result

    return None


def check_diag(board, inv=False):
    diag = [board[i][SIZE - i - 1 if inv else i] for i in xrange(SIZE)]
    return check_row(diag)


def transpose(board):
    return zip(*board)


def check_state(board):
    row_result = check_rows(board)
    if row_result:
        return "%s won" % row_result

    col_result = check_rows(transpose(board))
    if col_result:
        return "%s won" % col_result

    diag1_result = check_diag(board)
    if diag1_result:
        return "%s won" % diag1_result

    diag2_result = check_diag(board, inv=True)
    if diag2_result:
        return "%s won" % diag2_result

    if is_finished(board):
        return "Draw"

    return "Game has not completed"


if __name__ == "__main__":
    T = int(raw_input())
    for t in xrange(T):
        board = read_board()
        print "Case #%d: %s" % (t + 1, check_state(board))
