#!/usr/bin/env python
import sys

f = open(sys.argv[1])

cases = int(f.readline())

for case in xrange(0, cases):
    result = None
    board = []
    line = f.readline().strip()
    board.append([])
    for i in line:
        board[0].append(i)

    board.append([])
    line = f.readline().strip()
    board[1] = []
    for i in line:
        board[1].append(i)

    board.append([])
    line = f.readline().strip()
    board[2] = []
    for i in line:
        board[2].append(i)

    board.append([])
    line = f.readline().strip()
    board[3] = []
    for i in line:
        board[3].append(i)

    if result is None:
        # Check for horizontal wins
        for row in xrange(0, 4):
            test_val = board[row][0]
            if test_val == 'T':
                test_val = board[row][1]  # Use the next value over to determine the current test piece

            if test_val == 'X':
                if 'O' not in board[row] and '.' not in board[row]:
                    result = 'X won'
                    break
            if test_val == 'O':
                if 'X' not in board[row] and '.' not in board[row]:
                    result = 'O won'
                    break

    if result is None:
        # Check for vertical wins
        for col in xrange(0, 4):
            test_val = board[0][col]
            if test_val == "T":
                test_val = board[1][col]

            if test_val == 'X':
                column = [board[r][col] for r in xrange(0, 4)]
                if 'O' not in column and '.' not in column:
                    result = 'X won'
                    break
            if test_val == 'O':
                column = [board[r][col] for r in xrange(0, 4)]
                if 'X' not in column and '.' not in column:
                    result = 'O won'
                    break

    if result is None:
        # Check one diagonal
        test_val = board[0][0]
        if test_val == 'T':
            test_val = board[1][1]
        diagonal = [board[i][i] for i in xrange(0, 4)]
        if test_val == 'X':
            if 'O' not in diagonal and '.' not in diagonal:
                result = "X won"
        if test_val == 'O':
            if 'X' not in diagonal and '.' not in diagonal:
                result = "O won"

    if result is None:
        #Check the other diagonal
        test_val = board[3][0]
        if test_val == 'T':
            test_val = board[2][1]
        diagonal = [board[3-c][c] for c in xrange(0, 4)]
        if test_val == 'X':
            if 'O' not in diagonal and '.' not in diagonal:
                result = "X won"
        if test_val == 'O':
            if 'X' not in diagonal and '.' not in diagonal:
                result = "O won"

    if result is None:
        result = "Draw"
        for row in xrange(0, 4):
            if '.' in board[row]:
                result = "Game has not completed"
                break

    print "Case #%s: %s" % (case+1, result)
    # Read the empty line between cases
    f.readline()
