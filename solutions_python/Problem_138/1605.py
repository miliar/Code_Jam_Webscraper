#!/usr/bin/env python

T = input()

for t in xrange(T):
    N = input()
    A = map(float, raw_input().split())
    B = map(float, raw_input().split())
    A.sort()
    B.sort()
    
    # War
    i = j = 0
    while True:
        if i == N or j == N: break
        if A[i] > B[j]:
            j += 1
        else:
            i += 1
            j += 1
    s0 = N - i
    
    # Deceitful War
    i = j = s1 = 0
    while True:
        if i == N or j == N: break
        if A[i] > B[j]:
            s1 += 1
            i += 1
            j += 1
        else:
            i += 1

    print 'Case #%d: %d %d' % (t+1, s1, s0)
