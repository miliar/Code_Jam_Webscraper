
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
    AC = int(parts[0])
    AJ = int(parts[1])

    CD = []
    for i in range(AC):
        parts = get_line().split()
        a = int(parts[0])
        b = int(parts[1])
        CD.append((a, b))
    CD = sorted(CD)

    JK = []
    for i in range(AJ):
        parts = get_line().split()
        a = int(parts[0])
        b = int(parts[1])
        JK.append((a, b))
    JK = sorted(JK)

    if AC > AJ:
        AC, AJ = AJ, AC
        CD, JK = JK, CD

    '''
    cd = [(c/60.0, d/60.0) for (c, d) in CD]
    jk = [(c/60.0, d/60.0) for (c, d) in JK]
    print "CD", CD, cd
    print "JK", JK, jk
    '''

    if AC == 0 and AJ == 1:
        if JK[0][1] <= 720 or JK[0][0] >= 720:
            return 2
        return 2

    if AC == 0 and AJ == 2:
        if JK[0][0] >= 720 or JK[1][1] <= 720:
            return 2
        if JK[1][1] - JK[0][0] <= 720:
            return 2
        if JK[1][0] - JK[0][1] >= 720:
            return 2
        return 4
    
    if AC == 1 and AJ == 1:
        if CD > JK:
            CD, JK = JK, CD

        if CD[0][1] <= 720 and JK[0][0] >= 720:
            return 2

        return 2
        
    return -1   


T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
