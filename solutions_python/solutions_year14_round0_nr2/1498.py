#!/usr/bin/env python
import math
import sys
import os
from os import system

def min_time(C, F, X):
	wait = float(X)/2
	buy = C/2
	new_wait = buy + ((X)/(2+F))
	buy = buy + C/(2+F)
	i = 2
	while new_wait < wait:
		rate = 2 + F*i
		wait = new_wait
		new_wait = buy + ((X)/rate)
		buy = buy + C/rate 
		i += 1
	return wait 
		
fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for t in range(T):
	tokens = fp.readline().split()
	C = float(tokens[0])
	F = float(tokens[1])
	X = float(tokens[2])

	ret = round(min_time(C,F,X), 7)

	fout.write('Case #%d: %f\n'%((t+1),ret))
