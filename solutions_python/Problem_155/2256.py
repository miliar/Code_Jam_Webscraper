#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def solve(Smax, S):
    n = 0
    stood = 0
    for i, s in enumerate(S):
        if i > stood:
            lack = i - stood
            n += lack
            stood += lack
        stood += s

    return n
    
    
# main
me = sys.argv[0].split("/")[-1].replace(".py", "")
#file = me + "-sample"
file = me + "-small-attempt0"
file = me + "-large"

with open(file + ".in", "r") as fdin:
    with open(file + ".out", "w") as fdout:

        T = int(fdin.readline())
        for ncase in range(T):
            Smax, shyness = fdin.readline().split()
            Smax = int(Smax)
            S = [int(d) for d in shyness]

            result = solve(Smax, S)
    
            line = "Case #%d: %d" % (ncase + 1, result)
            print(line) 
            fdout.write("%s\n" % line)
    