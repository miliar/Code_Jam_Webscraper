
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


def calc():
    parts = get_line().split();
    s = [1 if ch == '-' else 0 for ch in parts[0]]
    k = int(parts[1])

    ans = 0
    for i in range(0, len(s) - k + 1):
        if s[i]:
            for j in range(i, i + k):
                s[j] = 1 - s[j]
            ans += 1
    return "IMPOSSIBLE" if 1 in s else ans

T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
