#!/usr/bin/env python

board_size = 4
def has_won(player, board):
    # Check row
    for row in board:
        if row.replace('T', player) == player * board_size:
            return True

    # Check cols
    cols = zip(*board)
    for col in cols:
        if ''.join(col).replace('T', player) == player * board_size:
            return True

    diag1 = ''.join([board[i][board_size - j - 1] for i in range(board_size) for j in range(board_size) if i == j])
    diag2 = ''.join([board[i][j] for i in range(board_size) for j in range(board_size) if i == j])

    if diag1.replace('T', player) == player * board_size or diag2.replace('T', player) == player * board_size:
       return True

    return False

def incomplete(board):
    for row in board:
        if '.' in row:
            return True

def get_status(board):
    if has_won('X', board):
        status = 'X won'
    elif has_won('O', board):
        status = 'O won'
    elif incomplete(board):
        status = 'Game has not completed'
    else:
        status = 'Draw'

    return status

if __name__ == '__main__':
    tc = int(raw_input())
    for t in range(tc):
        board = []
        for i in range(board_size):
            board.append(raw_input().strip())
        if t != tc - 1:
            raw_input()
        print 'Case #%d: %s' % (t + 1, get_status(board))
            
