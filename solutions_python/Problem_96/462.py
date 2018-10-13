#!/usr/bin/python
import sys

m = {}
sm = {}

for i in range(11):
    for j in range(11):
        for k in range(11):
            s = i + j + k
            if abs(i - j) <= 1 and abs(i - k) <= 1 and abs(j - k) <= 1:
                if s not in m:
                    m[s] = max(i, j, k)
                else:
                    m[s] = max(m[s], i, j, k)
            if max(i, j, k) - min(i, j, k) <= 2:
                if s not in sm:
                    sm[s] = max(i, j, k)
                else:
                    sm[s] = max(sm[s], i, j, k)


T = int(sys.stdin.readline())
for i in range(T):
    l = sys.stdin.readline().split(' ')
    n, s, p = int(l[0]), int(l[1]), int(l[2])
    ans = 0
    for j in range(n):
        t = int(l[3 + j])
        if m[t] >= p:
            ans = ans + 1
        elif s > 0 and sm[t] >= p:
            ans = ans + 1
            s = s - 1
    print 'Case #%d: %d' % (i + 1, ans)


