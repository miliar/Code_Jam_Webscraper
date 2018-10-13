#!/usr/bin/env python

import sys

def check_horizontal(board, row, ch):
    for sq in board[row]:
        if sq != 'T' and sq != ch:
            return False
    return True

def check_vertical(board, col, ch):
    for row in xrange(4):
        if board[row][col] != 'T' and board[row][col] != ch:
            return False
    return True

def check_diagonol1(board, ch):
    for i in xrange(4):
        if board[i][i] != 'T' and board[i][i] != ch:
            return False
    return True

def check_diagonol2(board, ch):
    for i in xrange(4):
        if board[i][3-i] != 'T' and board[i][3-i] != ch:
            return False
    return True

def main():
    T = int(sys.stdin.readline())
    for test_case in xrange(1, T+1):
        board = [ list(sys.stdin.readline().strip()) for _ in xrange(4) ]
        sys.stdin.readline()

        empty = 0
        for row in board:
            for sq in row:
                if sq == '.':
                    empty += 1

        o_win = False
        x_win = False
        for i in xrange(4):
            o_win = o_win or check_horizontal(board, i, 'O')
            x_win = x_win or check_horizontal(board, i, 'X')

            o_win = o_win or check_vertical(board, i, 'O')
            x_win = x_win or check_vertical(board, i, 'X')
        o_win = o_win or check_diagonol1(board, 'O') or check_diagonol2(board, 'O')
        x_win = x_win or check_diagonol1(board, 'X') or check_diagonol2(board, 'X')

        if x_win:
            message = "X won"
        elif o_win:
            message = "O won"
        elif empty == 0:
            message = "Draw"
        else:
            message = "Game has not completed"
        print "Case #%d: %s" % (test_case, message)

if __name__ == '__main__':
    main()
