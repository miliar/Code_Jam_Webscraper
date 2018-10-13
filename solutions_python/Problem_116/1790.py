#!/usr/bin/env python

import fileinput

def won(board, player):
    # horizontal
    for row in board:
        count = 0
        for col in row:
            if col is player or col is 'T':
                count += 1
        if count is 4:
            return True
    # vertical
    board_t = map(list, zip(*board))
    for row in board_t:
        count = 0
        for col in row:
            if col is player or col is 'T':
                count += 1
        if count is 4:
            return True
    # diagonal
    count = 0
    for i in range(0, 4):
        if board[i][i] is player or board[i][i] is 'T':
            count += 1
    if count is 4:
            return True
    count = 0
    for i in range(0, 4):
        if board[i][4-i-1] is player or board[i][4-i-1] is 'T':
            count += 1
    if count is 4:
            return True
    return False

def is_completed(board):
    for row in board:
        for col in row:
            if col is '.':
                return False
    return True


def solve(board, case):
    if won(board, 'X'):
        print "Case #%d: X won" % case
    elif won(board, 'O'):
        print "Case #%d: O won" % case
    elif is_completed(board):
        print "Case #%d: Draw" % case
    else:
        print "Case #%d: Game has not completed" % case

cases = 0
board = []
current_case = 0
current_line = 0
for line in fileinput.input():
    line = line.strip()
    current_line += 1
    if current_line is 1:
        cases = int(line)
        continue
    if len(line) is 0:
        board = []
        continue
    row = list(line)
    board.append(row)
    assert len(row) is 4
    if len(board) is 4:
        current_case += 1
        solve(board, current_case)

