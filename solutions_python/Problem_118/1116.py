#!/usr/bin/python3

import sys


def case():
    A, B = [int(x) for x in sys.stdin.readline().split()]
    p = [1,4, 9,121,484]
    r =0
    for i in p:
        if i >= A and i <=B: r += 1
    return r

T = int(sys.stdin.readline())
for i in range(1,T+1):
    print("Case #%s: %s" % (i, case()))
    

