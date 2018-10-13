#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def checkInvoke(c1,c2,invoke):
    for inv in invoke:
        if (inv[0] == c1 and inv[1] == c2) or(inv[0] == c2 and inv[1] == c1):
            return [inv[2],]
    return [c1,c2]

def checkFusion(output,opposed):
    output_set = set(output)
    for f in opposed:
        if f[0] in output_set and f[1] in output_set:
            return []
    return output



if len(sys.argv) !=2:
    sys.exit()

f = open(sys.argv[1],"r")

T = 0
i = 0
for line in f:
    i = i + 1
    if i == 1:
        T = int(line)
    else:
        case = line.strip().split(" ")
        #print case
        cur = 0
        C = int(case[cur])
        invoke = case[cur + 1:cur + C+1]
        cur = cur + C + 1
        #print C,invoke
        D = int(case[cur])
        opposed = case[cur+1:cur+D+1]
        #print D,opposed
        cur = cur + D + 1
        N = int(case[cur])
        input = case[-1]
        #print invoke,opposed,input

        y = []
        for n in input:
            y += [n,]
            while len(y) >= 2:
                out = checkInvoke(y[-2],y[-1],invoke)
                if len(out) == 1:
                    y = y[:-2] + out
                else:
                    break
            y = checkFusion(y,opposed)
        k = 0
        if len(y) == 0:
            out = "[]"
        else:
            out = "["
            for member in y:
                k = k + 1
                if k == len(y):
                    out += member +"]"
                else:
                    out += member +", "
        print "Case #%d:" % (i-1),out


