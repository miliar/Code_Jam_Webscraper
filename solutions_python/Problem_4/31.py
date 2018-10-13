#!/usr/bin/env python
import sys
import math

def readCJIn(filename):
	"""Reads the file.
	
	This function reads Google Code Jam input files and returns the number of inputs and a list containing the inputs"""
	file = open(filename)
	inputs = []
	for line in file:
		inputs.append(line.strip())
	file.close()
	return int(inputs[0]),inputs[1:len(inputs)]

def feq(a,b):
	"""Returns true if the difference between a and b are less than 1e-6"""
	if math.fabs(a-b)<0.000001:
		return True
	return False

def getAngle(x1,y1,x2,y2,x3,y3,z1=0,z2=0,z3=0):
	x1dif,x3dif,y1dif,y3dif,z1dif,z3dif = (x1-x2),(x3-x2),(y1-y2),(y3-y2),(z1-z2),(z3-z2)
	return math.acos((x1dif*x3dif + y1dif*y3dif + z1dif*z3dif)/(math.sqrt((x1dif**2+y1dif**2+z1dif**2))*math.sqrt((x3dif**2+y3dif**2+z3dif**2))))

def getPolygonArea(vertices):
	vsize = len(vertices)-1
	area = 0
	
	for i in xrange(0,vsize):
		xcurr,ycurr = vertices[i]
		xnext,ynext = vertices[i+1]
		area += (xcurr*ynext)-(xnext*ycurr)
	
	return area/2

inmag, inputs = readCJIn(sys.argv[1])

for i in range(0,inmag):
	input = inputs[0:3]
	n = int(input[0])
	inputs = inputs[3:]
	v1 = [int(x) for x in input[1].split()]
	v2 = [int(x) for x in input[2].split()]
	v1.sort()
	v2.sort()
	dot = 0
	for j in range(0,n):
		k = n-j-1
		dot += v1[j]*v2[k]
	print "Case #%d: %d"%(i+1,dot)
