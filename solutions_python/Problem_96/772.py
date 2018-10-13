#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def solve(data):
    N, S, p, *scores = [int(x) for x in data]
    if len(scores) != N:
        print("Input error: ", data)
    # print("N: %d, S: %d, p: %d" % (N, S, p))
    
    cand = []
    for score in scores:
        cand.append(findcand(score))

    return exhaust(cand, S, p)

def exhaust(cand, surprise, p):
    if len(cand) == 0:
        return 0

    slist = [0]
    for root in cand[0]:
        sp = surprise - spchk(root)
        if sp < 0 or (len(cand) == 1 and sp != 0):
            continue
        s = gechk(root, p) 
        slist.append(s + exhaust(cand[1:], sp, p))
    return max(slist)

def spchk(scores):
    if scores[1] - scores[0] == 2 \
        or scores[2] - scores[0] == 2 \
        or scores[2] - scores[1] == 2:
        return 1
    else:
        return 0

def gechk(scores, p):
    if max(scores) >= p:
        return 1
    else:
        return 0
        
def findcand(score):
    cand = []
    # assume a <= b <= c
    a_low = max(0, score - 10 - 10)
    for a in range(a_low, 11):
        for b in range(a, a + 3):
            c = score - a - b
            if b > c:
                break
            if c <= b + 2 and c <= a + 2:
                cand.append([a, b, c])
    return cand
    
# main
file = "B-sample"
file = "B-small-attempt0"
#file = "B-large"

with open(file + ".in", "r") as fdin:
    with open(file + ".out", "w") as fdout:

        T = int(fdin.readline())
        for ncase in range(T):
            data = fdin.readline().split()
            
            # print("Case #%d:" % (ncase + 1))
            result = solve(data)
    
            line = "Case #%d: %d" % (ncase + 1, result)
            print(line) 
            fdout.write("%s\n" % line)
