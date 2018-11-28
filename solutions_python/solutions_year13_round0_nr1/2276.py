import sys

def transpose(board):
    return [''.join(nr) for nr in zip(*[list(r) for r in board])]

def has_winner(row):

    row = row.replace('T', '')

    # row should be string
    if all([c == 'X' for c in row]):
        return 'X'
    elif all([c == 'O' for c in row]):
        return 'O'
    else:
        return False

def determine_state(board):

    draw_possible = '.' not in ''.join(board)
    tboard = transpose(board)

    for i in range(4):
        v = has_winner(board[i]) or has_winner(tboard[i])
        if v:
            return '%s won' % v

    dv = has_winner(''.join([board[i][i]for i in range(4)])) or has_winner(''.join([board[3-i][i] for i in range(4)]))
    if dv:
        return '%s won' % dv

    if draw_possible:
        return 'Draw'
    else:
        return 'Game has not completed'

    return state


if __name__ == '__main__':

    N = int(sys.stdin.readline().strip())

    for i in range(N):
        board = []
        for _ in range(4):
            board.append(sys.stdin.readline().strip())
        sys.stdin.readline() # empty
        print 'Case #%s: %s' % (i+1, determine_state(board))

