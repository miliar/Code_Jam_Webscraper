# -*- coding: utf-8 -*-

import sys
import math

def solve(data):
    l = [float(s) for s in str(data).split(' ')]
    c = l[0]    # amount for buying cookie farm
    f = l[1]    # extra cookie per second for each farm
    x = l[2]    # objective

    crt = 2.0

    # calculate tipping point by mathematical formula
    n = int(math.ceil((x / c) - 1 - (2 / f)))
    if n < 0:
        return x / crt

    total = 0.0
    for i in range(n):
        total += c / crt
        crt += f
    total += x / crt
    return total

def process(inp):
    inp = [str(s).strip() for s in inp]
    crt_n = 0
    total_n = int(inp[crt_n])
    crt_n += 1
    for i in range(total_n):
        result = solve(inp[crt_n])
        crt_n += 1
        print "Case #%d: %.7f" % (i + 1, result)

if __name__ == "__main__":
    process(str(sys.stdin.read()).split('\n'))