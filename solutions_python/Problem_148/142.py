#!/usr/bin/python

def solve(N, X):
    S = map(int, raw_input().split())
    S.sort()
    while len(S) > 1:
        if S[0] + S[-1] <= X:
            N -= 1
            S = S[1:-1]
        else:
            S = S[:-1]
    return N

T = int(raw_input())
for i in range(T):
    print "Case #%i: %s" % (i+1, solve(*(int(s) for s in raw_input().split(' '))))
