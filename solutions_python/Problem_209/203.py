
import math
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
    ps = []
    for i in range(N):
        parts = get_line().split()
        R = int(parts[0])
        H = int(parts[1])
        ps.append((-R, -R*H))


    ps = sorted(ps)

    # -R*H, -R
    ps = [(k, i)  for (i, k) in ps]

    #print ps

    ans = 0

    for i in range(N):
        if i + K - 1 > N - 1:
            break
        
        cans = ps[i + 1:]
        cans = sorted(cans)
        
        t = 0
        for j in range(K - 1):
            a, b = cans[j]
            t += -a
        t += -ps[i][0]

        t *= 2 * math.pi

        t += ps[i][1]*ps[i][1]*math.pi

        #print i, t

        if t > ans:
            ans = t
            
    
    return ans


T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
