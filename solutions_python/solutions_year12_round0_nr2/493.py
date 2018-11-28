#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import sys

def debug(a): sys.stderr.write(str(a) + '\n')
def readarray(foo): return [foo(e) for e in raw_input().split()]
def readint(): return int(raw_input().strip())

debug = lambda x: None


def count(N, S, p, points):
    """
    N: a number of Googlers
    S: a possible number of surprising triplets
    p: the least score result required
    points: total scores of Googlers

    [0, 3 * p - 4) : the best result is less than p
    [3 * p - 4, 3 * p - 2) : if the best result is p then surprising
    [3 * p - 2, 3 * p] : if the best result is p then not surprising

    surprising_lowest = 3 * p - 4
    not_surprising_lowest = 3 * p - 2

    p = 0
    (0, 0, 0): not surprising
    -> surprising_lowest = N/A (0)
       not_surprising_lowest = 0

    p = 1
    (0, 0, 1): not surprising
    -> surprising_lowest = N/A (1)
       not_surprising_lowest = 1

    p >= 2
    (p, p - 2, p - 2), (p, p - 1, p - 2): surprising
    (p, p - 1, p - 1), (p, p, p - 1), (p, p, p): not surprising
    -> surprising_lowest = 3 * p - 4
       not_surprising_lowest = 3 * p - 2
    """
    assert N == len(points)

    if p < 2:
        surprising_lowest = p
    else:
        surprising_lowest = 3 * p - 4

    if p < 2:
        not_surprising_lowest = p
    else:
        not_surprising_lowest = 3 * p - 2

    result = 0
    for point in points:
        if point < surprising_lowest:
            debug('#1: {0}'.format(point))
            continue
        elif point < not_surprising_lowest:
            debug('#2: {0}'.format(point))
            if S > 0:
                debug('#2-1: {0}'.format(point))
                result += 1
                S -= 1
            continue
        else:
            debug('#3: {0}'.format(point))
            result += 1

    return result

T = readint()
for i in xrange(T):
    ints = readarray(int)
    N = ints.pop(0)
    S = ints.pop(0)
    p = ints.pop(0)
    points = ints
    print('Case #{0}: {1}'.format(i + 1, count(N, S, p, points)))
