#import string,itertools,fractions,heapq,re,array,bisect
#from math import *
#from collections import Counter
def rl(s): return xrange(len(s))


INF = 2147483647


import sys
stdin = sys.stdin

T =        int( stdin.readline().strip() )

for icase in range(1, T+1):
    N, P = map(int, stdin.readline().strip().split())
    gs =   map(int, stdin.readline().strip().split())

    rr = 0
    by_mod = [0] * P
    for g in gs:
        if g % P == 0:
            rr += 1
        else:
            by_mod[g % P] += 1

    if 2 == P:
        rr += (by_mod[1] + 1) // 2
    else:
        k = min(by_mod[1], by_mod[P-1])
        rr += k
        by_mod[1] -= k
        by_mod[P-1] -= k
        further = []
        if 4 == P:
            rr += by_mod[2] // 2
            if by_mod[2] % 2 == 1:
                further.append(2)
        further.extend([1] * by_mod[1])
        further.extend([P-1] * by_mod[P-1])
        m = 0
        for f in further:
            if 0 == m:
                rr += 1
            m = (m + f) % P

    print "Case #%d:" % icase, rr


