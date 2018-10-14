#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
from operator import xor

def solve(vals):
    if reduce(xor, vals):
        return "NO"
    return sum(vals) - min(vals)

def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        sys.stdin.readline()
        numbers = map(int, sys.stdin.readline().split())
        ret = solve(numbers)
        print "Case #" + str(i+1) + ": " + str(ret)

if __name__ == '__main__':
    main()
