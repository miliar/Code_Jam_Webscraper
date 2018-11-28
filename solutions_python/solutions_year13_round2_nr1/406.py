#!/usr/bin/env python

def inputs():
    return tuple(map(int, raw_input().split(' ')))

def f(A, S, R):
    if len(S) == 0:
        return 0
    if A > S[0]:
        return min(R, f(A+S[0], S[1:], min(R, len(S)-1)))
    else:
        if R > 0:
            return min(R, 1 + f(2*A-1, S, R-1))
        else:
            return R

(T,) = inputs()
for i in range(T):
    print "Case #%d:" % (i+1,),
    (A, N) = inputs()
    S = sorted(inputs())
    print f(A, S, len(S))
