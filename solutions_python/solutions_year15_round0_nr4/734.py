#!/usr/bin/env python
#coding=utf8
tests = input()
res = []
for test in range(0, tests):
	line = raw_input()
	X = int(line.split()[0])
	R = int(line.split()[1])
	C = int(line.split()[2])

	if (R*C)%X != 0:
		res.append('RICHARD')
		continue
	elif (X>2 and min(R,C)*2<=X) or max(R,C)<X:
		res.append('RICHARD')
		continue
	elif X>=7:
		res.append('RICHARD')
		continue
	else:
		res.append('GABRIEL')
	
for i in range(0, tests):	 
	print "Case #" + str(i+1) + ": " + str(res[i])

