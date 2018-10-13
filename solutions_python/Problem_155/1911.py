#!/usr/bin/python3

import sys

def case():
    M, S = sys.stdin.readline().split()
    M = int(M)
    S = [int(x) for x in S]
    invite = 0
    total = 0
    for i in range(M + 1):
        n = max(0, i - total)
        invite += n
        total += S[i] + n
    return invite

T = int(sys.stdin.readline())
for i in range(1,T+1):
    print("Case #%s: %s" % (i, case()))
    

