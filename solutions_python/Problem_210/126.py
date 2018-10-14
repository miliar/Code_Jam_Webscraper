#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
f = open('B-test.in','r')
g = open('B-test.ou','w')"""

f = open('B-small-attempt0.in','r')
g = open('B-small-attempt0.ou','w')

"""f = open('B-large.in','r')
g = open('B-large.ou','w')"""


def solution(C, J):
    if len(C) == 1:
        return 2
    elif len(C) == 2:
        C.sort()
        if C[1][1]-C[0][0] <= 720 or C[1][0]-C[0][1] >= 720:
            return 2
        else:
            return 4
    elif len(J) == 2:
        J.sort()
        if J[1][1]-J[0][0] <= 720 or J[1][0]-J[0][1] >= 720:
            return 2
        else:
            return 4
    else:
        return 2

n = int(f.readline()[:-1])
for k in range(n):
    line = f.readline()[:-1].split(' ')
    AC = int(line[0])
    AJ = int(line[1])
    C = []
    J = []
    for i in range(AC):
        line_i = f.readline()[:-1].split()
        Ci = int(line_i[0])
        Di = int(line_i[1])
        C += [(Ci, Di)]
    for i in range(AJ):
        line_i = f.readline()[:-1].split()
        Ji = int(line_i[0])
        Ki = int(line_i[1])
        J += [(Ji, Ki)]
    g.write('Case #'+str(k+1)+': '+str(solution(C, J))+'\n')



f.close()
g.close()