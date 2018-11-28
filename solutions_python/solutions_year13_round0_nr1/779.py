#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def makeArray(board):
    result = []
    result.append(board[0])
    result.append(board[1])
    result.append(board[2])
    result.append(board[3])

    result.append([board[0][0], board[1][0], board[2][0], board[3][0]])
    result.append([board[0][1], board[1][1], board[2][1], board[3][1]])
    result.append([board[0][2], board[1][2], board[2][2], board[3][2]])
    result.append([board[0][3], board[1][3], board[2][3], board[3][3]])

    result.append([board[0][0], board[1][1], board[2][2], board[3][3]])
    result.append([board[0][3], board[1][2], board[2][1], board[3][0]])

    return result


def judge(sym):
    if '.' in sym:
        return False
    while 'T' in sym:
        sym.remove('T')

    first = sym[0]
    if sym.count(first) == len(sym):
        return first
    else:
        return False;


def judge2(sym_list):
    for a in sym_list:
        res = judge(a)
        if res == False:
            continue
        else:
            return res
    return False

T = int(sys.stdin.readline())

for i in range(0, T):
    board = [list(sys.stdin.readline().rstrip("\n")) for x in range(0, 4)]
    sys.stdin.readline()
    sym_list = makeArray(board)
    won = judge2(sym_list)
    if won != False:
        print "Case #%d: %s won" % (i+1, won)
    else:
        tmp = []
        for a in board:
            tmp.extend(a);
        if '.' in tmp:
            print "Case #%d: Game has not completed" % (i+1)
        else:
            print "Case #%d: Draw" % (i+1)

