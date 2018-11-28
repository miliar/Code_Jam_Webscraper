#import string,itertools,fractions,heapq,re,array,bisect
#from math import *
from collections import defaultdict
def rl(s): return xrange(len(s))


INF = 2147483647


import sys
stdin = sys.stdin

T =        int( stdin.readline().strip() )

for icase in range(1, T+1):
    N, C, M = map(int, stdin.readline().strip().split())
    aa = defaultdict(int)
    bb = defaultdict(int)
    for i in range(M):
        Pi, Bi = map(int, stdin.readline().strip().split())
        if Bi == 1:
            aa[Pi-1] += 1
        else:
            bb[Pi-1] += 1

    rr = 0
    pairs = []
    for k in aa.keys():
        for i in range(aa[k]):
            found = False
            for b in bb:
                if b == k:
                    continue
                found = True
                bb[b] -= 1
                if bb[b] == 0:
                    del bb[b]
                rr += 1
                pairs.append((k, b))
                break
            if found:
                aa[k] -= 1
                if aa[k] == 0:
                    del aa[k]
    #print "pairs", pairs
    pr = 0
    if len(aa) != 0 != len(bb):
        left = None
        for k in aa:
            left = k
            break
        other_pairs = 0
        for a, b in pairs:
            if a != left != b:
                other_pairs += 1
        need = min(aa[left], bb[left])
        decreased = min(need, other_pairs)
        rr += decreased
        al = aa[left] - decreased
        bl = bb[left] - decreased
        if left == 0:
            rr += al + bl
        else:
            rr += min(al, bl)
            pr = min(al, bl)
            rr += abs(al - bl)
    else:
        for k in aa:
            rr += aa[k]
        for k in bb:
            rr += bb[k]

    print "Case #%d:" % icase, rr, pr
        

    



