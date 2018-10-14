#!/usr/bin/python

import sys

ns = [0]*31
s = [-1]*31

for i in xrange(1,31):
    if i % 3 == 0:
        ns[i] = i // 3
        s[i] = i // 3 + 1
    elif i % 3 == 1:
        ns[i] = i // 3 + 1
        s[i] = i // 3 + 1
    elif i % 3 == 2:
        ns[i] = i // 3 + 1
        s[i] = i // 3 + 2

i = iter(map(int, sys.stdin.read().split()))

T = next(i)
for case in xrange(1,T+1):
    N = next(i)
    S = next(i)
    p = next(i)
    t = iter(sorted((next(i) for n in xrange(N)), reverse=True))

    result = 0
    while True:
        try:
            ti = next(t)
            if ns[ti] >= p:
                result += 1
            elif s[ti] >= p and S > 0:
                result += 1
                S -= 1
            else:
                break
        except:
            break

    print "Case #%d:" % case, result
