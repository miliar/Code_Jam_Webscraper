#!/usr/bin/env python
# Oversized Pancake Flipper
from math import *
from sys import *

numcases = int(stdin.readline())


def flip(i,k, cakes):
    for j in range(i,i+k):
        if cakes[j] == "+":
            cakes[j] = "-"
        else:
            cakes[j] = "+"

for case in range(1,numcases+1):
    count = 0
    data = stdin.readline().split()
    k = int(data[1])
    cakes = list(data[0])
    for i in range(len(cakes)-k+1):
        if cakes[i] == "-":
            count += 1
            flip(i,k,cakes)

    print "Case #" + str(case) + ":",
    if "-" in cakes:
        print "IMPOSSIBLE"
    else:
        print str(count)


