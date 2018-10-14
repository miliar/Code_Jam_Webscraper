#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
import sys

def solve(N, M, lawn):
    hcol = []
    for row in range(N):
        hcol.append(max(lawn[row]))
    hrow = []
    for col in range(M):
        hrow.append(max([lawn[row][col] for row in range(N)]))
    
    for row in range(N):
        for col in range(M):
            if lawn[row][col] != min(hcol[row], hrow[col]):
                return "NO"
    return "YES"
    
    
# main
me = sys.argv[0].split("/")[-1].replace(".py", "")
file = me + "-sample"
file = me + "-small-attempt0"
file = me + "-large"

with open(file + ".in", "r") as fdin:
    with open(file + ".out", "w") as fdout:

        T = int(fdin.readline())
        for ncase in range(T):
            N, M = [int(x) for x in fdin.readline().split()]
            lawn = []
            for i in range(N):
                data = [int(x) for x in fdin.readline().split()]
                assert len(data) == M
                lawn.append(data)
            
            result = solve(N, M, lawn)
    
            line = "Case #%d: %s" % (ncase + 1, result)
            print(line) 
            fdout.write("%s\n" % line)
    