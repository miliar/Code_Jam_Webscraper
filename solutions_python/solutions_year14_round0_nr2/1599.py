#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import *
import sys

if __name__ == "__main__":
    t = input()
    for caseIdx in xrange(1,t+1):
        c, f, x = map(float, raw_input().split())
        time = 0
        rate = 2
        while x/rate > (x/(rate+f)+c/rate):
            time += c/rate
            rate += f
        time += x/rate
        print "Case #%d: %.7f" % (caseIdx, time)
