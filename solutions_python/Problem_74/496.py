#!/usr/bin/env python
import math
import sys
import os
from os import system

def calculate(robot, poslist, olist, blist):
	odiff = []
	bdiff = []
	#print olist, blist
	if len(olist) > 0:
		odiff.append(olist[0]-1)
	if len(blist) > 0:
		bdiff.append(blist[0]-1)
	for i in range(len(olist)-1):
		odiff.append(math.fabs(olist[i+1]-olist[i]))
	for i in range(len(blist)-1):
		bdiff.append(math.fabs(blist[i+1]-blist[i]))
	#print odiff
	#print bdiff

	oidx = 0
	bidx = 0
	opos = 0
	bpos = 0
	step = 0
	owait = 0
	bwait = 0
	prev = ''
	for i in range(len(robot)):
		color = robot[i]
		pos = poslist[i]
		if color is 'O':
			need = max(odiff[oidx] - owait,0) 
			step = step + need + 1
			oidx += 1
			if prev is 'O':
				bwait += (need + 1)
			else :
				bwait = need + 1
				owait = 0
			prev = 'O'
		if color is 'B':
			need = max(bdiff[bidx] - bwait,0)
			step = step + need + 1
			bidx += 1
			if prev is 'B':
				owait += (need + 1)
			else :
				owait = need + 1
				bwait = 0
			prev = 'B'
	
	return step


fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	l = fp.readline().split()
	N = int(l[0])
	index = 1
	robot = []
	pos = []
	o = []
	b = []
	#print l
	for j in range(N):
		r = l[index]
		p = int(l[index+1])
		index += 2
		robot.append(r)
		pos.append(p)
		if r is 'O':
			o.append(p)
		elif r is 'B':
			b.append(p)

	#print robot
	#print pos
	#print o
	#print b
	
	ret = calculate(robot, pos, o, b)

	fout.write('Case #%d: %d\n'%((i+1),ret))
