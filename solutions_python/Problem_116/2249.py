#!/usr/bin/env python

import sys
import itertools

def open_input(file):
    try:
        f = open(file, "r")
        return f
    except:
        print "can not open ", file
        sys.exit(1)

def made_line(board, x):
    # check row
    for r in xrange(4):
        count = 0
        for c in xrange(4):
            if board[r][c] != x and board[r][c] != 'T':
                break
            else:
                count += 1
        if count == 4:
            return True

    # check column
    for c in xrange(4):
        count = 0
        for r in xrange(4):
            if board[r][c] != x and board[r][c] != 'T':
                break
            else:
                count += 1
        if count == 4:
            return True

    # check diagonal
    if ((board[0][0] == x or board[0][0] == 'T') and
        (board[1][1] == x or board[1][1] == 'T') and
        (board[2][2] == x or board[2][2] == 'T') and
        (board[3][3] == x or board[3][3] == 'T')) :
        return True
    if ((board[0][3] == x or board[0][3] == 'T') and
        (board[1][2] == x or board[1][2] == 'T') and
        (board[2][1] == x or board[2][1] == 'T') and
        (board[3][0] == x or board[3][0] == 'T')) :
        return True

    return False

def game_completed(board):
    for r in xrange(4):
        for c in xrange(4):
            if board[r][c] == '.':
                return False
    return True

def do_solve(board):
    if made_line(board, 'X'):
        return "X won"
    if made_line(board, 'O'):
        return "O won"
    if game_completed(board):
        return "Draw"
    else:
        return "Game has not completed"

def solve(input):
    """ T = # test case """
    T = int(input.readline())

    for i in range(T):
        # 4 x 4 board
        board = [['.' for x in xrange(4)] for x in xrange(4)]
        for x in xrange(4):
            board_row = input.readline().rstrip()
            board[x][0] = board_row[0]
            board[x][1] = board_row[1]
            board[x][2] = board_row[2]
            board[x][3] = board_row[3]
        input.readline().rstrip() # empty line
        print "Case #{0}: {1}".format(i+1, do_solve(board))

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(open_input(sys.argv[1]))
    else:
        print 'require input'
        sys.exit(1)
