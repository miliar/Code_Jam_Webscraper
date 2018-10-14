#!/usr/bin/python3
from sys import stdin
def x(s):
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return x(str(int(s[:i+1]) - 1)) + len(s[i+1:]) * '9'
    return s

T = int(stdin.readline())
for i in range(T):
    print('Case #{0:d}: {1:d}'.format(i+1, int(x(stdin.readline().rstrip()))))
