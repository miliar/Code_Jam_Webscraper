#!/usr/bin/env python

def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)

te = int(raw_input())
for i in range(1, te + 1):
    t = raw_input().split(' ')
    n = int(t[0])
    M = 0
    for j in range(1, n + 1):
        for k in range(j + 1, n + 1):
            l = abs(int(t[j]) - int(t[k]))
            M = nwd(M, l)
    ret = (M - int(t[1])) % M;
    print 'Case #' + str(i) + ': ' + str(ret)

