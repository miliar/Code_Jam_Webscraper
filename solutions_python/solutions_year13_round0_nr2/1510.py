#!/usr/bin/env python


from logging import debug

def show(a):
    for line in a:
        debug(' '.join(line))


def solve(i, a, N, M):
    p = 'Case #{0}: '.format(i + 1)
    result = {
        'Y': p + 'YES',
        'N': p + 'NO',
    }

    if N != len(a):
        raise Exception('N != len(a)')
    if M != len(a[0]):
        raise Exception('M != len(a[0])')

    rowMax = [0 for i in range(N)]
    colMax = [0 for i in range(M)]

    for y in range(N):
        for x in range(M):
            if a[y][x] > rowMax[y]:
                rowMax[y] = a[y][x]
            if a[y][x] > colMax[x]:
                colMax[x] = a[y][x]
    debug(rowMax)
    debug(colMax)

    for y in range(N):
        for x in range(M):
            if a[y][x] >= rowMax[y] or a[y][x] >= colMax[x]:
                pass
            else:
                return result['N']
    return result['Y']


from sys import argv
from os.path import basename, splitext
from logging import basicConfig, DEBUG, INFO

if "__main__" == __name__:
    level=INFO
    if 0:
        level=DEBUG
    basicConfig(format='%(levelname)s: %(message)s', level=level)
    infname = argv[1]
    oufname = splitext(basename(infname))[0] + '.out'
    with open(infname, 'r') as inf:
        with open(oufname, 'w') as ouf:
            n = int(inf.readline())
            debug(n)
            for i in range(n):
                (N, M) = (int(x) for x in inf.readline().strip().split(' '))
                debug(str(N) + ' ' + str(M))
                a = []
                for n in range(N):
                    a.append(inf.readline().strip().split(' '))
                show(a)
                ouf.write(solve(i, a, N, M) + '\n')
