# coding=utf-8

# Created on 
# Code Jam 2017 qr c
# @author: manolo

import sys

ifile = sys.stdin
ofile = sys.stdout


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def solve(stalls, clients):

    while True:
        n = max(stalls)
        stalls.remove(n)

        if clients == 1:
            if n == 1:
                return 0, 0
            if n == 2:
                return 1, 0
            if n % 2 != 0:
                return n/2, n/2
            else:
                return n/2, n/2 - 1

        if n % 2 != 0:
            stalls.extend([n/2, n/2])
        else:
            stalls.extend([n/2 - 1, n/2])

        clients -= 1


T = int(r())
for case in range(1, T+1):
    n, k = r().split(' ')
    what = solve([int(n)], int(k))
    w(case, '{} {}'.format(*what))

