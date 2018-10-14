#!/usr/bin/python -u
# encoding: utf-8

from __future__ import unicode_literals


inputFile = "/Users/XinDong/Desktop/A-large.in.txt"


def solveLine(line):
    cps = line.split(' ')
    mc = int(cps[0])
    psum = 0
    need = 0
    i = 0
    while i < mc+1:
    	digit  = int(cps[1][i])
    	if psum < i:
    		need += i-psum
    		psum += i-psum
    	psum += digit
    	i +=1
    return need




lcounter = 0

with open(inputFile) as input:
    for l in input:
        if lcounter>0:
            opmin = solveLine(l)
            print "Case #{}: {}".format(lcounter, opmin)
        lcounter +=1

