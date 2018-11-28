#! /usr/bin/python
import os
import sys
import glob
from math import sqrt

if len(sys.argv) != 2:
	print 'USAGE: q1.py input.in'
	sys.exit()

fIn = open(sys.argv[1], 'r')
param = fIn.readline().split()
num = int(param[0])
for i in range(num):
	line = fIn.readline()[:-1]
	N = int(line.split()[0])
	K = int(line.split()[1])
	if (K +1 ) % (2**N) == 0:
		print 'Case #'+str(i+1)+': ON'
	else: 
		print 'Case #'+str(i+1)+': OFF'

#	print 'Case #'+str(i+1)+': '+str(count)
#	tokens = ['' for i in range(L)]
#	print '\n'
