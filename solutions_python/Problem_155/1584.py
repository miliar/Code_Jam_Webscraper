#!/usr/bin/env python2

T = input()
for t in range(1, T+1):
    Smax, S = raw_input().split()
    Smax = int(Smax)
    S = [int(i) for i in S]

    ans = 0
    s = S[0]
    for i in range(1, Smax + 1):
        if s < i:
            ans += i - s
            s += i - s
        s += S[i]
    print 'Case #' + str(t) + ': ' + str(ans)
