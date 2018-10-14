import sys


def check_string(s):
    xs, os, ts, dots = [s.count(x) for x in ['X', 'O', 'T', '.']]
    if xs + ts == 4:
        return 'X won', dots
    elif os + ts == 4:
        return 'O won', dots
    return False, dots


def check_board(board):
    total_dots = 0
    columns = [''.join([row[x] for row in board]) for x in range(4)]
    diagonals = [''.join([board[0][0], board[1][1], board[2][2], board[3][3]]),
                 ''.join([board[0][3], board[1][2], board[2][1], board[3][0]])]
    for s in board + columns + diagonals:
        r, dots = check_string(s)
        if r:
            return r
        total_dots += dots
    if total_dots == 0:
        return 'Draw'
    else:
        return 'Game has not completed'


def main():
    lines = list(sys.stdin)
    cases = int(lines[0])
    boards = [[x.rstrip() for x in lines[x:x+5][0:4]] for x in range(1, cases * 5, 5)]
    for i, board in enumerate(boards):
        print 'Case #%s: %s' % (i + 1, check_board(board))

if __name__ == '__main__':
    main()
