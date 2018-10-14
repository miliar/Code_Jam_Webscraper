#!/usr/bin/python
# Google Code Jam 2008
# Problem 2-A
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


class Node:
	def ide(self):
		return self._id

	def setId(self, i):
		self._id = i
	def rchild(self):
		return self._rchild

	def lchild(self):
		return self._lchild

	def setLchild(self, n):
		self._lchild = n

	def setRchild(self, n):
		self._rchild = n

	def setType(self, t):
		self.ty = t

	def type(self):
		return self.ty

	def changable(self):
		return self.c

	def setChangable(self, b):
		self.c = b

	def setValue(self, v):
		self.val = v

	def value():
		return self.val

	def compVal():
		if self.ty == 1:
			return self._rchild.compVal() and self._lchild.compVal()
		if self.ty == 0:
			return self._rchild.compVal() or self._lchild.compVal()
		return self.val

cache = {}
def calcVal(D, i):
	if D[i][0] == -1:
		globals()["cache"][i] = D[i][1]
		return D[i][1]
	if D[i][0] == 1:
		if calcVal(D, 2*i) and calcVal(D, 2*i+1):
			globals()["cache"][i] = 1
			return 1
		else:
			globals()["cache"][i] = 0
			return 0
	if D[i][0] == 0:
		if calcVal(D, 2*i) or calcVal(D, 2*i+1):
			globals()["cache"][i] = 1
			return 1
		else:
			globals()["cache"][i] = 0
			return 0

def calcChanges(D, i, v):
	if calcVal(D,i) == v:
		return 0

	if D[i][0] == 0:
		if v == 1:
			return min(calcChanges(D,2*i, v), calcChanges(D,2*i+1, v))
		else: # v == 0
			if D[i][1]:
				if calcVal(D,2*i) == 0 or calcVal(D,2*i+1) == 0:
					return 1
				else:
					return 1 + min(calcChanges(D,2*i, v), calcChanges(D,2*i+1, v))
			else:
				return calcChanges(D,2*i, v) + calcChanges(D,2*i+1, v)

	if D[i][0] == 1:
		if v == 0:
			return min(calcChanges(D,2*i, v), calcChanges(D,2*i+1, v))
		else: # v == 1
			if D[i][1]:
				if calcVal(D,2*i) == 1 or calcVal(D,2*i+1) == 1:
					return 1
				else:
					return 1 + min(calcChanges(D,2*i, v), calcChanges(D,2*i+1, v))
			else:
				return calcChanges(D,2*i, v) + calcChanges(D,2*i+1, v)

	return 1000000
	

def solve(caseNum):
	M, V = map(int, sys.stdin.readline().strip().split(" "))

	globals()["cache"] = {}
	
	D = {}
	for i in range((M-1)/2):
		g, c = map(int, sys.stdin.readline().strip().split(" "))
		i += 1
		D[i] = (g,c)
		last = i
	
	for i in range((M+1)/2):
		v = int(sys.stdin.readline().strip())
		D[i+last+1] = (-1,v)
	

	total = calcChanges(D, 1, V)

	if total >= 1000000:
		sys.stdout.write("Case #%d: IMPOSSIBLE" % (caseNum))
	else:
		sys.stdout.write("Case #%d: %s" % (caseNum, total))

# ---------------------------------------------------------------------------------------------------------------

casesCount = int(re.findall(r'[\d]+', sys.stdin.readline())[0])
first = True
for case in range(1, casesCount + 1):
	if(first):
		first = False
	else:
		print ""
	solve(case)
