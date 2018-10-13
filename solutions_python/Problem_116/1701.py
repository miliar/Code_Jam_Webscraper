#!/usr/bin/env python

def show(t):
    for line in t:
        debug(line)
    debug('\n')


def transpose(t):
    tt = []
    for y in range(4):
        temp = ''
        for x in range(4):
            temp = temp + t[x][y]
        tt.append(temp)
    return tt


def diag(t, main=True):
    result = ''
    for i in range(4):
        if main:
            result = result + t[i][i]
        else:
            result = result + t[i][3-i]
    debug(result)
    return result


def check(p, t):
    debug('check ' + p)

    tt = transpose(t)
    show(t)
    show(tt)
    ref = 4*p
    for i in range(4):
        if ref == t[i] or ref == tt[i]:
            return True

    debug('checking diags')
    if ref == diag(t) or ref == diag(t, main=False):
        return True

    debug(p + ' is not won')
    return False


def is_dot(a):
    for line in a:
        if -1 != line.find('.'):
            return True
    return False


def solve(i, t):
    p = 'Case #{0}: '.format(i + 1)
    result = {
        'X': p + 'X won',
        'O': p + 'O won',
        'D': p + 'Draw',
        'N': p + 'Game has not completed',
    }

    for player in ['O', 'X']:
        table = [s.replace('T', player) for s in a]
        if check(player, table):
            return result[player]

    if is_dot(a):
        return result['N']
    return result['D']




from os.path import basename, splitext
from sys import argv
from logging import debug, basicConfig, DEBUG


if "__main__" == __name__:
    # basicConfig(format='%(levelname)s: %(message)s', level=DEBUG)
    with open(argv[1], 'r') as f:
        with open(splitext(basename(argv[1]))[0] + '.out', 'w') as ouf:
            n = int(f.readline())
            for i in range(n):
                a = []
                for l in range(4):
                    a.append(f.readline().strip())
                f.readline()
                ouf.write(solve(i, a) + '\n')
