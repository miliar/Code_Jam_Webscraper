#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def compute(line):
    l = line.split(" ")
    nb_googlers = int(l[0])
    nb_surprised = int(l[1])
    p = int(l[2])
    if p > 0:
        min_normal = p*3-2
    else:
        min_normal = 0

    if p > 1:
        min_surprised = p*3-4
    else:
        min_surprised = 1

    nb = 0
    for v in l[3:]:
        i = int(v)
        if i >= min_normal:
            nb += 1
        elif i >= min_surprised and nb_surprised > 0:
            nb_surprised -= 1
            nb += 1
    return nb
            

f=open(sys.argv[1])
lines=f.read().split("\n")
nb_lines=int(lines[0])
lines=lines[1:]

for i in range(nb_lines):
    print("Case #%d: %d" % (i+1, compute(lines[i])))
