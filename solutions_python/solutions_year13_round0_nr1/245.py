#!/usr/bin/python
import sys

def check(board, player):
    winchar = 'T'+player
    def check_line(line):
        return all((ch in winchar) for ch in line)
    for row in board:
        if check_line(row):
            return True
    for col in zip(*board):
        if check_line(col):
            return True
    if check_line(board[i][i] for i in xrange(4)):
        return True
    if check_line(board[i][3-i] for i in xrange(4)):
        return True
    return False

def solve(board):
    if check(board, 'X'):
        return "X won"
    elif check(board, 'O'):
        return "O won"
    elif any(row.count('.') for row in board):
        return "Game has not completed"
    else:
        return "Draw"

num_cases = int(sys.stdin.readline())
for test_case in xrange(1,num_cases+1):
    board = []
    for row in xrange(4):
        board.append(sys.stdin.readline().strip())
    print "Case #{0}: {1}".format(test_case, solve(board))
    sys.stdin.readline()
