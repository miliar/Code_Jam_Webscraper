#!/usr/bin/env python

import sys


def checkLine(l):
    for cl in l:
        #print  " > [%s]" % cl
        if cl.count('O') == 4:
            return (True, 'O won')
        if cl.count('X') == 4:
            return (True, 'X won')
        if cl.count('O') == 3 and cl.count('T') == 1:
            return (True, 'O won')
        if cl.count('X') == 3 and cl.count('T') == 1:
            return (True, 'X won')

    return (False, 'Unknown')


def boardNotFull(B):
    for i in range(4):
        if B[i].count('.') > 0:
            return True
    return False


def solve(B):
    if B[0][0] != '.':
        l1 = B[0]
        l2 = ''.join([B[j][0] for j in range(4)])
        d1 = ''.join([B[j][j] for j in range(4)])
        (status, result) = checkLine([l1, l2, d1])
        if status:
            return result

    if B[3][3] != '.':
        l1 = B[3]
        l2 = ''.join([B[j][3] for j in range(4)])
        (status, result) = checkLine([l1, l2])
        if status:
            return result

    if B[3][0] != '.':
        d1 = ''.join([B[j][3 - j] for j in range(4)])
        (status, result) = checkLine([d1])
        if status:
            return result

    if B[1][1] != '.':
        l1 = B[1]
        l2 = ''.join([B[j][1] for j in range(4)])
        (status, result) = checkLine([l1, l2])
        if status:
            return result

    if B[2][2] != '.':
        l1 = B[2]
        l2 = ''.join([B[j][2] for j in range(4)])
        (status, result) = checkLine([l1, l2])
        if status:
            return result

    if boardNotFull(B):
        return "Game has not completed"
    else:
        return "Draw"


def main(infile):
    n = int(infile.readline())
    for i in range(n):
        #B = [[c for c in infile.readline().rstrip()] for j in range(4)]
        B = [infile.readline().rstrip() for j in range(4)]
        infile.readline()
        print 'Case #%s: %s' % (i + 1, solve(B))

main(sys.stdin)
