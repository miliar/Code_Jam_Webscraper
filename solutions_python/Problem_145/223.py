#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# google code jam - c.durr - 2014

# Part Elf
# https://code.google.com/codejam/contest/3004486/dashboard
# 

# 

from math      import *
from sys       import *
from fractions import *

def readint():    return int(stdin.readline())
def readarray(f): return map(f, stdin.readline().split())
def readstring(): return stdin.readline().strip()
	
def solve(f):
	k = -1
	for g in range(40):
		f *= 2
		if f>=1:
			f-=1
			if k==-1:
				k = g+1
	if f==0:
		return k
	else:
		return -1

for test in range(readint()):
	f = readarray(Fraction)[0]
	g = solve(f)
	print "Case #%i:"% (test+1), ("impossible" if g==-1 else g)
    
    
