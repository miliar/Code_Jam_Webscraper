

import sys
sn = sys.stdin


def couldBeSurprising(n):
    return 2 <= n <= 28

def maxNonSurprising(n):
    k = n / 3
    if n % 3 != 0:
        k += 1
    return k

def maxSurprising(n):
    base = (n - 2) / 3
    return base + 2


T = int(sn.readline())
for tcase in range(T):
    tokens = map(int, sn.readline().strip().split())
    N, S, p = tokens[:3]
    ts = tokens[3:]

    re = 0
    sleft = S
    for it in ts:
        if maxNonSurprising(it) >= p:
            re += 1
        elif couldBeSurprising(it) and maxSurprising(it) >= p and sleft >= 1:
            re += 1
            sleft -= 1




    
    print "Case #%d:" % (tcase+1), re


