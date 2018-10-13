from sys import stdin
from math import log

def adds2hop(l, L):
    return int(log((L-1)/(l-1), 2)) + 1

def absorb(l, L, n):
    return L + (2**n)*l - 2**n + 1

T = int(raw_input())
tt = 0
while tt < T:
    tt += 1
    A, N = map(int, stdin.readline().split())
    motes = sorted(map(int, stdin.readline().split()))
    ops = 0
    if A == 1:
        ops = len(motes)
    else:
        for mi in xrange(N):
            if A <= motes[mi]:
                nHopes = adds2hop(A, motes[mi])
                if nHopes >= N - mi:
                    ops += N - mi
                    break
                else:
                    ops += nHopes
                    A = absorb(A, motes[mi], nHopes)
            else:
                A += motes[mi]
    
    print "Case #%d: %d" % (tt, ops)
    
