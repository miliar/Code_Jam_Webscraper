#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-
#
# © 2014 Peter Volkov (pva)


with open("A-small-attempt0.in", "r") as f:
    lines = f.readlines()

N = int(lines[0])
n = 0
case = 0
while case < N:
    n = 1 + 10*case
    case += 1
    line = int(lines[n])
    A = set(int(i) for i in lines[n+line].split())
    #print(A)
    n += 5
    line = int(lines[n])
    B = set(int(i) for i in lines[n+line].split())
    #print(B)
    C = set.intersection(A, B)
    #print(C)
    if len(C) == 0:
        print("Case #%s: Volunteer cheated!" % case)
    if len(C) == 1:
        print("Case #%s: %s" % (case, C.pop()))
    if len(C) > 1:
        print("Case #%s: Bad magician!" % case)

