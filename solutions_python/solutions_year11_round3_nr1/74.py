from __future__ import division
import sys, string
import itertools

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

A = []
R,C = 0,0

def chk():
	for r in range(R):
		for c in range(C):
			if A[r][c] == '#':
				return 1
	return 0
	
def red():
	for r in range(R-1):
		for c in range(C-1):
			if A[r][c] == '#' and A[r+1][c] == '#' and A[r][c+1] == '#' and A[r+1][c+1] == '#':
				A[r][c], A[r+1][c], A[r][c+1], A[r+1][c+1] = "/", "\\", "\\", "/"
				return 1
	return 0
	
for t in range(T):
	R, C = readlist()
	A = []
	for i in range(R):
		ln = list(sys.stdin.readline().strip())
		A.append(ln)
	
	#~ print A
	
	while red():
		pass
	print "Case #%d:" % (t+1)
	if chk():
		print "Impossible"
	else:
		for i in range(R):
			print string.join(A[i], '')
