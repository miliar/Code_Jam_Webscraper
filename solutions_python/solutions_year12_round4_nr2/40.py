#!/usr/bin/python
#B.py
#Author: James Damore
#Created on: May 26, 2012
#Time-stamp: <2012-05-26 11:41:12>
#cat Downloads/B-small-attempt0.in | ~/B.py > output.txt

import sys, math, collections, Queue
import numpy as np

def dbgln(a): sys.stderr.write(str(a) + "\n")
def read_ints(lines=None, fmt=int):
    if lines is None: return map(int, raw_input().split())
    return [map(fmt, raw_input().split()) for _ in range(lines)]


def read_input():
    N, W, L = read_ints()
    R = read_ints()
    R = sorted([(r, i) for i, r in enumerate(R)])[::-1]
    positions = [(0, 0), (W, L)]
    #if N > 2:
    #    if R[2][0] + R[0][0] < L:
    #        positions.append((0, L))
    #        if N > 3:
    #            if R[3][0] + R[0][0] < L:
    #        positions.append((W, 0))
    #    else:
    #        positions.append((W, 0))
    #        positions.append((0, L))
    for i in range(2, N):
        for _ in range(100000):
            next = (np.random.rand() * W, np.random.rand() * L)
            for j in range(i):
                if ((positions[j][0] - next[0]) ** 2 + \
                    (positions[j][1] - next[1]) ** 2) ** 0.5 < R[j][0] + R[i][0]:
                    break
            else:
                positions.append(next)
                break
        else:
            dbgln("FAIL")
            return "FAIL"
    
    output = ["" for _ in range(N)]
    for i, r in enumerate(R):
        output[r[1]] =  str(positions[i][0]) + " " + \
                        str(positions[i][1])
    return " ".join(output)


numCases=input()
for i in range(1, numCases+1):
    #read_input()
    dbgln(i)
    output = read_input()
    print "Case #%d:" % i, output
