#!/usr/bin/python2.7

import sys

def read_input(boards, file):
    cases = 0

    with open(file, "r") as fp:
        cases = fp.readline().strip('\n')

        board = ''
        #count = 0
        #for line in fp:
        #    if line == '\n':
        #        boards.append(board)
        #        count = 0
        #        board = []
        #        continue
        #    if count <= 4:
        #        board.append(line.strip('\n'))
        #        count += 1
        #boards.append(board)

        for line in fp:
            if line == '\n':
                continue
            board += line.strip('\n')
            if len(board) == 16:
                boards.append(board)
                board = ''

    return cases, boards

#def check_vertical():
#
#
#def check_horizontal(board):
#    for row in board:
#        if row.count('.') >= 1:
#            continue
#        if row.count('X') >= 3:
#            if row.count('T'):
#                return "X"
#            if row.count(')'):
#                return -1
#            return "X"
#        if row.count('O') >= 3:
#            if row.count('T'):
#                return "O"
#            if row.count('X'):
#                return -1
#            return "O"
#
#    return -1
#def check_diagonal():

def rewriteBoard(direction, board):
    rBoard = []

    if direction == "vertical":
        for i in range(4):
            rBoard.append(board[i::4])
    if direction == "horizontal":
        for i in range(0,16,4):
            rBoard.append(board[i:i+4])
    if direction == "ldiagonal":
        for i in range(0, 16, 5):
            rBoard.append(board[i])
        rBoard = [''.join(rBoard)]
    if direction == "rdiagonal":
        for i in range(3, 15, 3):
            rBoard.append(board[i])
        rBoard = [''.join(rBoard)]

    #print rBoard
    return rBoard

def checkBoard(direction, board):
    board = rewriteBoard(direction, board)
    for row in board:
        if row.count('.') >= 1:
            continue
        if row.count('X') == 4 or row.count('X') == 3 and row.count('T'):
            return "X"
        if row.count('O') == 4 or row.count('O') == 3 and row.count('T'):
            return "O"

    # Nobody won, it's a draw
    if row.count('.') == 0:
        return -1

    return 1

#def decide_winner(results):
    #print check_horizontal(board)
    #if check_horizontal(board):
            continue
        if row.count('X') == 4 or row.count('X') == 3 and row.count('T'):
            return "X"
        if row.count('O') == 4 or row.count('O') == 3 and row.count('T'):
            return "O"

    # Nobody won, it's a draw
    if row.count('.') == 0:
        return -1

    return 1

#def decide_winner(results):
    #print check_horizontal(board)
    #if check_horizontal(board):
    #if check_vertical(board):
    #if check_diagonal(board):
    #
    #print "Case

def parse_boards(cases, boards):
    count = 1
    directions = ["horizontal", "vertical", "ldiagonal", "rdiagonal"]

    for board in boards:
        #sum([checkBoard(direction, board) for direction in directions])
        res = [checkBoard(direction, board) for direction in directions]
        #print res
        if res.count("X"):
            print "Case #%d: X won" % count
        elif res.count("O"):
            print "Case #%d: O won" % count
        elif res.count(-1) == 4:
            print "Case #%d: Draw" % count
        else:
            print "Case #%d: Game has not completed" % count
        #for res in [checkBoard(direction, board) for direction in directions]:
        #    if res == "X" or res == "O":
        #        print "Case #%d: %s won" % (count, res)
        #    if res == 1
        #    print "RES", res
        count += 1

cases, boards = read_input([], sys.argv[1])
#print cases
#print cases, boards
parse_boards(cases, boards)
#rewriteBoard("vertical", boards[0])
