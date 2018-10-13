#!/usr/bin/python

import sys
import math

#f = open('A-small.in')

f = sys.stdin


test_cases = int(f.readline().strip())

case_num = 1


def center( A,B,C ):
    return ( ( A[0] + B[0] + C[0] ) / 3., (A[1] +  B[1] + C[1] ) / 3. )


def perms(l):
    perms = []
    for i in range(0, len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                perms.append([l[i], l[j], l[k]])
    return perms
                

for i in range(test_cases):
    ( n , A, B, C, D, x0, y0, M) = [ int(x) for x in f.readline().strip().split() ]
    tree_coords = []
    possible_tris = []
    X = x0
    Y = y0
    count = 0
    tree_coords.append( (X,Y) )
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        tree_coords.append( (X,Y) )
    possible_tris = perms(tree_coords)
    for p in possible_tris:
        c = center(*p)
        a0 = math.modf(c[0])
        a1 = math.modf(c[1])
        if a0[0] == 0 and a1[0] == 0:
            count += 1
    print "Case #%d: %d" % (case_num, count)
    case_num += 1
