#!/usr/bin/python3

import sys

def tidy(x):
    x = str(x)
    l = len(x)
    for i in range(l - 1):
        if x[i] > x[i + 1]:
            return tidy(int(x[:i + 1]) - 1) + '9' * (l - i - 1)
    return x  # x is tidy :-)

n = int(sys.stdin.readline())

for i in range(1, n+1):
    x = int(sys.stdin.readline())
    print('Case #{0}: {1}'.format(i, int(tidy(x))))
