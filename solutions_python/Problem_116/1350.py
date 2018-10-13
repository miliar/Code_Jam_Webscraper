#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

X_WIN = 'X won'
O_WIN = 'O won'
DRAW = 'Draw'
NOT_COMPLETED = 'Game has not completed'


def is_win_row(r):
    if (r[0] in 'XO' and
        r[0] == r[1] and r[1] == r[2] and r[0] == r[3]):
        return r[0]
    return None


def find_win_row(M):
    for r in M:
        c = is_win_row(r)
        if c:
            #print r
            return c
    return None


def board_transpose(M):
    MT = []
    for i in range(4):
        MT.append([M[j][i] for j in range(4)])
#    print M
#    print MT
    return MT


def is_win_diagonals(M):
    if (M[0][0] in 'XO' and
        M[0][0] == M[1][1] and M[0][0] == M[2][2] and M[0][0] == M[3][3]):
        return M[0][0]
    if (M[0][3] in 'XO' and
        M[0][3] == M[1][2] and M[0][3] == M[2][1] and M[0][3] == M[3][0]):
        return M[0][3]
    return None


def check_for_win(M, player_mark):
    MP = [r.replace('T', player_mark) for r in M]
    #print MP
    c = find_win_row(MP)
    if c:
        #print 'row win'
        return c
    c = is_win_diagonals(MP)
    if c:
        #print 'diagonal win'
        return c
    #print 'transpose'
    MPT = board_transpose(MP)
    c = find_win_row(MPT)
    if c:
        #print 'row win'
        return c
    return None


def check_for_symbol(M, x):
    for r in M:
        if x in r:
            return True
    return False


def solve(M):
    #print M
    c = check_for_win(M, 'X')
    if c is None:
        c = check_for_win(M, 'O')
    if c:
        if c == 'X':
            return X_WIN
        else:
            return O_WIN
    if check_for_symbol(M, '.'):
        return NOT_COMPLETED
    return DRAW


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


T = int(ifs.readline())
for t in range(1, T + 1):
    M = []
    for _ in range(4):
        M.append(ifs.readline().strip())
    ifs.readline()
    a = solve(M)
    ofs.write('Case #%d: %s\n' % (t, a))
