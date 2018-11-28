#!/usr/bin/python
# Google Code Jam 2008
# Problem 1B-A
# zzmike

import sys
import re
from Numeric import *
#from decimal import *

# ---------------------------------------------------------------------------------------------------------------

sys.setcheckinterval(10000)
PI = arccos(-1)
PI_2 = arccos(-1) / 2

#getcontext().prec = 200
#getcontext().rounding = ROUND_DOWN

# ---------------------------------------------------------------------------------------------------------------




def solve(caseNum):
	n, A, B, C, D, x0, y0, M = map(int, sys.stdin.readline().strip().split(" "))
	
	trees = []
	X = x0
	Y = y0
	trees.append((x0,y0))
	for i in range(1, n):
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		trees.append((X, Y))

	l = len(trees)
	res = 0
	for i in range(0, l):
		for j in range(i+1, l):
			for k in range(j+1, l):
				cx = float((trees[i][0] + trees[j][0] + trees[k][0])) / 3.0
				cy = float((trees[i][1] + trees[j][1] + trees[k][1])) / 3.0
				
				if cx == int(cx) and cy == int(cy):
					res += 1

	sys.stdout.write("Case #%d: %s" % (caseNum, res))

# ---------------------------------------------------------------------------------------------------------------

casesCount = int(re.findall(r'[\d]+', sys.stdin.readline())[0])
first = True
for case in range(1, casesCount + 1):
	if(first):
		first = False
	else:
		print ""
	solve(case)
