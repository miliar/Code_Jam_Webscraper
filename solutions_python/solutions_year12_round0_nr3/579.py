#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def shift(num, puissance):
    first = int(num/puissance)
    return ((num%puissance)*10)+first

def compute(line):
    l = line.split(" ")
    A = int(l[0])
    B = int(l[1])
    found = set()
    final = 0
    for i in range(A,B+1):
        if i in found:
            continue
        num = i
        puissance = 1
        tour = 0
        while num > 10:
            num /= 10
            puissance *= 10
            tour += 1
        maybe = i
        nb_pair = 0
        for j in range(tour+1):
            maybe = shift(maybe, puissance)
            if maybe >= A and maybe <= B and maybe >= puissance and maybe != i and maybe not in found:
                found.add(maybe)
                nb_pair += 1
        final += int((nb_pair*(nb_pair+1))/2)
    return final

f=open(sys.argv[1])
lines=f.read().split("\n")
nb_lines=int(lines[0])
lines=lines[1:]

for i in range(nb_lines):
    print("Case #%d: %d" % (i+1, compute(lines[i])))
