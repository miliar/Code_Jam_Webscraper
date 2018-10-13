# -*- coding: utf-8 -*-
from __future__ import division, print_function
from math import sqrt, ceil, floor
import random

def parse(f):
    lst = []
    f.next()
    for l in f:
        t = l.split()
        lst.append((t[0], int(t[1])))
    return lst


def pancakes(S, K):
    bistr = ''.join([("1" if a == "+" else "0") for a in S])
    b = int(bistr, 2)
    mask = int("1"*K, 2)
    nbxor = 0

    for l in range(len(S) - K + 1):
        if(bistr[l] == "0"):
            b = b ^ (mask << (len(S)-K-l))
            bistr = bin(b)[2:]
            bistr = "0"*(len(S) - len(bistr)) + bistr
            nbxor += 1
            if("0" not in bistr):
                break
    if("0" in bistr):
        return "IMPOSSIBLE"
    return str(nbxor)

def output(fw, inlst):
    for i, a in enumerate(inlst):
        k = pancakes(*a)
        print(i, k)
        fw.write("Case #" + str(i+1) + ": " + str(k) + "\n")


f = open("A-large.in", 'r')
fw = open("A-large.out", 'w')
output(fw, parse(f))
