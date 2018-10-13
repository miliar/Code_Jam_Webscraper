#!/usr/bin/env python
#-*- coding: utf-8 -*-

SIZE = 4
X = 'X'
O = 'O'
EMPTY = '.'
T = 'T'
NEW = 0
LOST = 'L'

def check_state(b):
    lines = [NEW] * SIZE
    columns = [NEW] * SIZE
    diag1 = NEW
    diag2 = NEW

    diag1_pos = [(0,0),(1,1),(2,2),(3,3)]
    diag2_pos = [(0,3),(1,2),(2,1),(3,0)]

    for i in xrange(len(b)):
        for j in xrange(len(b[i])):
            if b[i][j] == EMPTY:
                lines[i] = EMPTY
                columns[j] = EMPTY

                if (i,j) in diag1_pos:
                    diag1 = EMPTY
                elif (i,j) in diag2_pos:
                    diag2 = EMPTY

            elif b[i][j] in (X,O):
                if lines[i] == NEW or lines[i] == T:
                    lines[i] = b[i][j]
                elif lines[i] != b[i][j]:
                    if lines[i] != EMPTY:
                        lines[i] = LOST

                if columns[j] == NEW or columns[j] == T:
                    columns[j] = b[i][j]
                elif columns[j] != b[i][j]:
                    if columns[j] != EMPTY:
                        columns[j] = LOST

                if (i,j) in diag1_pos:
                    if diag1 == NEW or diag1 == T:
                        diag1 = b[i][j]
                    elif diag1 != b[i][j]:
                        if diag1 != EMPTY:
                            diag1 = LOST
                elif (i,j) in diag2_pos:
                    if diag2 == NEW or diag2 == T:
                        diag2 = b[i][j]
                    elif diag2 != b[i][j]:
                        if diag2 != EMPTY:
                            diag2 = LOST

            elif b[i][j] == T:
                if lines[i] == NEW:
                    lines[i] = T

                if columns[j] == NEW:
                    columns[j] = T

                if (i,j) in diag1_pos:
                    if diag1 == NEW:
                        diag1 = T
                elif (i,j) in diag2_pos:
                    if diag2 == NEW:
                        diag2 = T

    won_X = False
    won_O = False
    ended = True
    if X in lines or X in columns or diag1 == X or diag2 == X:
        won_X = True
    if O in lines or O in columns or diag1 == O or diag2 == O:
        won_O = True
    if EMPTY in lines or EMPTY in columns or diag1 == EMPTY or diag2 == EMPTY:
        ended = False

    if not won_X and not won_O:
        if ended:
            return 'Draw'
        else:
            return 'Game has not completed'
    elif won_X and won_O:
        return 'Draw'
    elif won_X:
        return 'X won'
    elif won_O:
        return 'O won'

for t in xrange(int(raw_input())):
    board = []
    for i in xrange(SIZE):
        board.append([x for x in raw_input()])
    raw_input()

    print 'Case #' + str(t+1) + ': ' + check_state(board)
