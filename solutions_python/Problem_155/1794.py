#!/usr/bin/python
# Author: vortex_ape
T = int(input())
for t in range(0, T):
    c = ans = 0
    n, s = input().split()
    n = int(n) + 1
    for i in range(0, n):
        if c < i:
            ans += i - c
            c = i
        c += int(s[i])
    print("Case #%d: %d" % (t+1, ans))
