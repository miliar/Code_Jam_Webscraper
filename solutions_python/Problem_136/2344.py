#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def solve(C, F, X):
    t = 0
    cookie_rate = 2
    while True:
        t1 = X/cookie_rate
        t2 = C/cookie_rate + X/(cookie_rate + F)
        if t1 <= t2:
            return t + t1
        t += C / cookie_rate
        cookie_rate += F
    
# main
me = sys.argv[0].split("/")[-1].replace(".py", "")
#file = me + "-sample"
#file = me + "-small-attempt0"
file = me + "-large"

with open(file + ".in", "r") as fdin:
    with open(file + ".out", "w") as fdout:

        T = int(fdin.readline())
        for ncase in range(T):
            C, F, X = [float(x) for x in fdin.readline().split()]

            result = solve(C, F, X)
    
            line = "Case #%d: %.7f" % (ncase + 1, result)
            print(line) 
            fdout.write("%s\n" % line)
    