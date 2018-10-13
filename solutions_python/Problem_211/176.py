
import os
import sys
import glob
import subprocess
import random
import fileinput
from collections import defaultdict


next_line = 0
lines = [line.strip() for line in fileinput.input()]
def get_line():
    global next_line
    i = next_line
    next_line += 1
    return lines[i]


def calc():
    parts = get_line().split()
    N = int(parts[0])
    K = int(parts[1])

    U = float(get_line())
    parts = get_line().split()
    ps = [float(i) for i in parts]
    ps = sorted(ps)

    ans = 0
    for i in range(N):
        a = (U + sum(ps[0:i+1])) / (i+1)
        if ps[i] > a:
            continue
        
        t = 1
        for j in range(N):
            if j <= i:
                t *= a
            else:
                t *= ps[j]
        if t > ans:
            ans = t

    return ans

T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
