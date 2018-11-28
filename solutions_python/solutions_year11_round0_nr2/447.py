#!/usr/bin/python3

from sys import stdin
from sys import stdout
from itertools import product

def match(s, ch1, ch2):
    if s[0] == ch1 and s[1] == ch2: return True
    if s[0] == ch2 and s[1] == ch1: return True
    return False

t = int(stdin.readline())
for i in range(1, t+1):
    line = stdin.readline().split()
    c = int(line[0])
    comb = line[1:c+1]
    d = int(line[c+1])
    opp = line[c+2:c+d+2]
    s = []
    seq = line[-1]
    for j in range(int(line[-2])):
        s.append(seq[j])
        if len(s) >= 2:
            p = next(filter(lambda x: match(x, s[-1], s[-2]), comb), None)
            q = next(filter(lambda x: match(x[0], x[1], s[-1]), product(opp, s[:-1])), None)
            if p:
                s[-2] = p[2]
                s.pop()
            elif q:
                s = []
    print('Case #{}: ['.format(i), end='')
    for j in range(len(s)-1):
        print(s[j], end=', ')
    if len(s) > 0: print(s[-1], end='')
    print(']')
