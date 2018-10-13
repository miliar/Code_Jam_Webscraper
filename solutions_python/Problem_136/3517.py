#!/usr/bin/python3
import sys
# import math
import fractions
# from array import array
sys.setrecursionlimit(100000)

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
    print('Case #{}:'.format(case+1), '{0:.7f}'.format(ans))


def solve(c, f, x, rate=2.0, t=0.0, max_time=float('inf')):
    if x <= c:
        return x/rate
    else:
        if (x-c)/rate <= x/(rate+f):
            return t + x/rate
        else:
            return solve(c, f, x, rate+f, t+c/rate)


def solve2(c, f, x, rate=2.0, t=0.0, max_time=float('inf')):
    if x <= c:
        return t + x/rate
    else:
        t += c/rate
        if t >= max_time:
            return max_time
        else:
            new_max = t + min((x-c)/rate, x/(rate+f))
            if new_max >= max_time:
                return max_time
            else:
                if (x-c)/rate <= x/(rate+f):
                    return t + (x-c)/rate
                else:
                    return solve(c, f, x, rate+f, t, new_max)


t = rl('i')
for case in range(t):
    c, f, x = rl('fff')
    output(case, solve2(c, f, x))
