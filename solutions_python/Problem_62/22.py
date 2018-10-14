#!/usr/bin/python

# google code jam - c.durr - 2010
# Rope Intranet
# regular expression matching


T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    ab = []
    for _ in range(N):
        Ai,Bi = map(int, raw_input().split())
        ab.append((Ai,Bi))
    ab.sort()
    L = []
    res = 0
    for Ai,Bi in ab:
        k = len([Bj for Bj in L if Bj > Bi])
        res = res + k
        L.append(Bi)
    
    print 'Case #%d:' % (t+1), res
