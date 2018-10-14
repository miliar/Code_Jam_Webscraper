#!/usr/bin/python

T = int(raw_input())
for t in range(T):
    S, K = raw_input().split()
    S = [s == '+' for s in S]
    K = int(K)
    
    n = 0
    
    i = 0
    while i <= len(S) - K:
        if not S[i]:
            n += 1
            for j in range(i, i + K):
                S[j] = not S[j]
        i += 1
    
    impossible = False
    for j in range(i, len(S)):
        if not S[j]:
            impossible = True
            break
    if impossible:
        n = "IMPOSSIBLE"
    print "Case #%d: %s" % (t + 1, n)