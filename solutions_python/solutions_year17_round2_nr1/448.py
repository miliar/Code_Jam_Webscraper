# -*- coding: utf-8 -*-
from __future__ import division, print_function
from math import sqrt, ceil, floor
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.setrecursionlimit(100000)

def parse(f):
    lst = []
    f.next()
    for l in f:
        D = int(l.split()[0])
        N = int(l.split()[1])
        horses = []
        for i in xrange(N):
            li = f.next()
            horses.append((int(li.split()[0]), int(li.split()[1])))
        lst.append((D, horses))
    return lst


def where(t, horses):
    return [min([a[0]+a[1]*t for i, a in enumerate(horses) if i >= j]) for i in xrange(len(horses))] 


def trajet(horses, D):
    h = horses[0]
    if len(horses) == 1:
        return ((D - h[0])/h[1])
    else:
        return max((D-h[0])/h[1], trajet(horses[1:], D))


def cruise(D, horses):
    horses.sort(key=lambda x: x[0])
    T = trajet(horses, D)
    return D/T
    



def output(fw, inlst):
    for i, a in enumerate(inlst):
        ret = cruise(*a)
        print(i, ret)
        fw.write("Case #" + str(i+1) + ": " + str(ret)+ "\n")


f = open("Alarge.in", 'r')
fw = open("A2017B.out", 'w')
output(fw, parse(f))

