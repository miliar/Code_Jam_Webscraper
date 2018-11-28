#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from decimal import *

def get_input(filename):
    fichier = open(filename, "r")
    data = fichier.read()
    fichier.close()
    return filter(None, data.split("\n"))

def time_to_get_farms(nf, c, f):
    ret = 0
    for i in range(nf):
        ret += c/(2+i*f)
    return ret

def time_to_finish(nf, f, x):
    return x/(2+nf*f)

def optimum_farm_number(c, f, x):
    nf = 0
    actual_time = time_to_finish(nf, f, x)
    while True:
        future_time = time_to_finish(nf+1, f, x) + time_to_get_farms(nf+1, c, f)
        if future_time > actual_time:
            return nf
        nf += 1
        actual_time = future_time
    
lines = []    
lines = get_input(sys.argv[1])
n = int(lines[0])
lines = lines[1:]

for i in range(n):
    C, F, X = map(float, lines[i].split())
    nf = optimum_farm_number(C, F, X)
    time = time_to_finish(nf, F, X) + time_to_get_farms(nf, C, F)
    print "Case #%d: %.7f" % (i+1, time)
