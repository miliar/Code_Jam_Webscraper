#!/usr/bin/python3
import sys
# import math
import fractions
# from array import array


def rl(convert='', a=False):
    line = sys.stdin.readline().split()
    for i, c in enumerate(convert):
        if c == 'i':
            line[i] = int(line[i])
        elif c == 's':
            pass
        elif c == 'f':
            line[i] = float(line[i])
    if not a and len(line) == 1:
        return line[0]
    return line


def gcd(*args):
    if len(args) == 0:
        return 0
    g = args[0]
    for i in range(1, len(args)):
        g = fractions.gcd(g, args[i])
    return g


def lcm(*args):
    if len(args) == 0:
        return 0
    g = args[0]
    for i in range(1, len(args)):
        g *= args[i]
    return g / gcd(*args)


def avg(a):
    return sum(a)/len(a)
# --------------------------------------------------------------------#

def output(case, ans):
    print('Case #{}:'.format(case+1), ans)

def read_round():
    a = rl('i')
    for r in range(4):
        row = set(rl('iiii'))
        if r == a-1:
            ret = row
    return ret

def solve(c, s):
    if len(s) == 0:
        output(c, 'Volunteer cheated!')
    elif len(s) == 1:
        output(c, next(iter(s)))
    else:
        output(c, 'Bad magician!')

t = rl('i')
for case in range(t):
    r1 = read_round()
    r2 = read_round()
    solve(case, r1 & r2)

