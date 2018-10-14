# -*- coding: utf-8 -*-
from __future__ import division, print_function
from math import sqrt, ceil, floor
import numpy as np
import math

def parse(f):
    lst = []
    f.next()
    for l in f:
        N = int(l.split()[0])
        K = int(l.split()[1])
        pancakes = []
        for i in range(N):
            line = f.next()
            pancakes.append((int(line.split()[0]), int(line.split()[1])))
        lst.append((K, pancakes))
    return lst

def syrup(K, pancakes):
    areamax = 0
    Rs = [p[0] for p in pancakes]
    for i, base in enumerate(pancakes):
        possible_stack = [p for j, p in enumerate(pancakes) if (p[0] <= base[0] and i != j)]
        possible_stack.sort(key=lambda x: x[0]*x[1], reverse=True)
        stack = possible_stack[0:K-1]
        area = math.pi*base[0]**2 + 2 * math.pi*(base[0]*base[1] + sum([p[0]*p[1] for p in stack]))
        if area > areamax:
            print([base]+stack)
            areamax = area
    return areamax

def output(fw, inlst):
    for i, a in enumerate(inlst):
        ret = syrup(*a)
        print(i, ret)
        fw.write("Case #{0}: {1:f} \n".format(i+1, ret))


f = open("A.in", 'r')
fw = open("A.out", 'w')
output(fw, parse(f))
