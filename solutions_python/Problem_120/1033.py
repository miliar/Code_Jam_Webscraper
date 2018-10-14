#! usr/bin/env python

import math

def needPaint(r, n):
    return 2 * n**2 + (2 * r - 1) * n

T = input()
T = int(T)

for TT in range(1, T + 1):
    r, t = input().split()
    r = int(r)
    t = int(t)
    ans = math.floor((math.sqrt((2 * r - 1)**2 + 8 * t) - 2 * r + 1) / 4)
    while needPaint(r, ans) > t:
        ans -= 1
    print("Case #" + str(TT) + ": " + str(ans))
