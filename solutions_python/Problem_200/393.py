
import os
import sys
import glob
import subprocess
import random
import fileinput


next_line = 0
lines = [line.strip() for line in fileinput.input()]
def get_line():
    global next_line
    i = next_line
    next_line += 1
    return lines[i]


def ok(s):
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return False
    return True

def calc():
    N = int(get_line())
    sn = str(N)
    if ok(sn):
        return N

    for i in range(len(sn) - 1, -1, -1):
        if sn[i] == '0':
            continue
        s = [ch for ch in sn]
        s[i] = chr(ord(s[i]) - 1)
        for j in range(i + 1, len(s)):
            s[j] = '9'
        s = ''.join(s)
        #print(s)
        if ok(s):
            return int(s)
    return ""


T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
