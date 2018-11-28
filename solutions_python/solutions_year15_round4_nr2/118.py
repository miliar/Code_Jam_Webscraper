
import os
import sys
import glob
import subprocess
import random
import fileinput
import operator


next_line = 0
lines = [line.strip() for line in fileinput.input()]


def get_line():
    global next_line
    i = next_line
    next_line += 1
    return lines[i]


def calc():
    s = get_line().split()
    N = int(s[0])
    V, X = float(s[1]), float(s[2])
    crs = [map(float, get_line().split()) for i in range(N)]
    crs = [(c, r) for r, c in crs]
    crs.sort()

    """
    print V, X
    print crs
    """
  
    ans = float('inf')
    for c, r in crs:
        if c-1e-6 <= X <= c+1e-6:
            t = V / r
            if t < ans:
                ans = t
    # print ans

    if len(crs) == 2 and crs[0][0] <= X and crs[1][0] >= X:
        x0, r0 = crs[0][0], crs[0][1]
        x1, r1 = crs[1][0], crs[1][1]
        if x0-1e-6 <= X <= x0+1e-6 and x1-1e-6 <= X <= x1+1e-6:
            t = V / (r0 + r1)
            if t < ans:
                ans = t

    if len(crs) == 2 and crs[0][0] <= X and crs[1][0] >= X:
        x0, r0 = crs[0][0], crs[0][1]
        x1, r1 = crs[1][0], crs[1][1]
        # print x0, r0
        # print x1, r1
        a0 = r0
        b0 = r1
        c0 = V
        a1 = r0*x0
        b1 = r1*x1
        c1 = V*X
        delta = a0*b1-a1*b0
        try:
            t0 = (c0*b1-c1*b0) / delta
            t1 = (c1*a0-c0*a1) / delta
            # print t0, t1
            t = max(t0, t1)
            if t < ans:
                ans = t
        except:
            pass

    if ans == float('inf'):
        return 'IMPOSSIBLE'
    return round(ans, 9)


T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
