#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

TEMPLATE = "Case #%d: %d"

def decode(input_str):
    line = input_str.split(" ")
    line = map(int, line)
    N = line[0]
    S = line[1]
    p = line[2]
    t = tuple(sorted(line[3:3+N], reverse=True))
    return (N, S, p, t)

def calculate(N, S, p, t):
    count = 0
    output = 0
    for i in t:
        if i >= 3 * p - 2 and i >= p:
            output += 1
        elif i >= 3 * p - 4 and i >= p and count < S:
            count += 1
            output += 1
    return output

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as r:
        T = int(r.readline())
        for i in xrange(T):
            line = r.readline().rstrip()
            N, S, p, t = decode(line)
            print TEMPLATE % (i + 1, calculate(N, S, p, t))
