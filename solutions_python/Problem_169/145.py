#!/usr/bin/env python3
# coding: UTF-8

import sys,math

DEBUG = True
DEBUG = False

qNum = int(sys.stdin.readline())
def debug(s1,s2):
    if DEBUG :
        print(str(s1) + ":" + str(s2))

def ans(q):
    a = 0

    l = sys.stdin.readline().strip().split(" ")
    N = int(l[0])
    V = float(l[1])
    X = float(l[2])

    if N == 1 :
        l = sys.stdin.readline().strip().split(" ")
        R = float(l[0])
        C = float(l[1])
        if C != X :
            print("Case #" + str(q) + ": IMPOSSIBLE")
        else :
            A = V/R
            print("Case #" + str(q) + ": " + str(round(A,7)))
        return

    l = sys.stdin.readline().strip().split(" ")
    R0 = float(l[0])
    C0 = float(l[1])
    l = sys.stdin.readline().strip().split(" ")
    R1 = float(l[0])
    C1 = float(l[1])
    debug("R",R0)
    if C0 > X and C1 > X :
        print("Case #" + str(q) + ": IMPOSSIBLE" )
        return
    if C0 < X and C1 < X :
        print("Case #" + str(q) + ": IMPOSSIBLE" )
        return
    if C0 == C1 :
        A = V/(R0+R1)
        print("Case #" + str(q) + ": " + str(round(A,7)))
        return

    if C0 == X :
        A = V/R0
        print("Case #" + str(q) + ": " + str(round(A,7)))
        return
    if C1 == X :
        A = V/R1
        print("Case #" + str(q) + ": " + str(round(A,7)))
        return

    T0 = ( X*V - V*C1 ) / ( R0 * C0 - R0 * C1 )
    debug("T0",T0)

    T1 = ( V - T0 * R0 ) / R1
    debug("T1",T1)

    if T0 < T1 :
        print("Case #" + str(q) + ": " + str(round(T1,7)))
    else :
        print("Case #" + str(q) + ": " + str(round(T0,7)))

    pass

for q in range(qNum):
    ans(q+1)
