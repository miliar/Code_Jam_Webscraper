import sys
from math import *
from copy import deepcopy
from itertools import product, permutations, combinations
from Queue import Queue


sys.setrecursionlimit(1500)

"""
def solve(m, r, c):
    for i in range(r):
        for j in range(c):
            if m[i][j] == '?':

                # ->
                for k in range(j + 1, c):
                    if m[i][k] != '?':
                        _m = deepcopy(m)
                        m[i][j] = m[i][k]
                        break

                # <-
                for k in range(0, j-1):
                    if m[i][k] != '?':
                        _m = deepcopy(m)
                        m[i][j] = m[i][k]
                        break
                # up
                for k in range(0, i - 1):
                    if m[k][j] != '?':
                        _m = deepcopy(m)
                        m[i][j] = m[k][j]
                        break

                # down
                for k in range(i + 1, r):
                    if m[k][j] != '?':
                        _m = deepcopy(m)
                        m[i][j] = m[k][j]
                        break
"""
def solve(_m, r, c):
    m = deepcopy(_m)

    for i in range(r):
        for j in range(c):
            if m[i][j] != '?':
                k = j - 1
                while k >= 0:
                    if m[i][k] == '?':
                        m[i][k] = m[i][j]
                    else:
                        break
                    k -= 1

                k = j + 1
                while k < c:
                    if m[i][k] == '?':
                        m[i][k] = m[i][j]
                    else:
                        break
                    k += 1

    for i in range(r):
        for j in range(c):
            if m[i][j] == '?':

                k = i + 1
                while k < r:
                    if m[k][j] != '?':
                        m[i][j] = m[k][j]
                        break
                    k += 1

                if m[i][j] == '?':
                    k = i - 1
                    while k >= 0:
                        if m[k][j] != '?':
                            m[i][j] = m[k][j]
                            break
                        k -= 1

    return m

for test in range(1, int(raw_input()) + 1):
    r, c = map(int, raw_input().split())

    m = [list(raw_input()) for _ in range(r)]

    ans = solve(m, r, c)

    print 'Case #{}:'.format(test)

    for r in ans:
        print ''.join(r)
