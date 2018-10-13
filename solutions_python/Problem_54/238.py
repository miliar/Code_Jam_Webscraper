#!/usr/bin/env python
# encoding: utf-8

import sys
import os
from fractions import gcd
from operator import sub

def main():
    c = int(sys.stdin.readline())
    for i in range(c):
        t = sorted(map(int, sys.stdin.readline().split())[1:])[:]
        g = reduce(gcd, map(sub, t[1:], t[:-1]))
        print "Case #%d: %d" % (i + 1, (t[0] + g - 1) // g * g - t[0])

if __name__ == '__main__':
	main()
