from __future__ import division
import sys, string
import itertools

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

A = []
def check(R0,C0,R,D):
	mi = 0
	mj = 0
	for i in range(R0, R0+R):
		for j in range(C0, C0+R):
			d = D + A[i][j]
			if (i,j) == (R0,C0) or (i,j) == (R0+R-1,C0+R-1): continue
			if (i,j) == (R0+R-1,C0) or (i,j) == (R0,C0+R-1): continue
			mi += d * (i - R0 - (R-1)/2)
			mj += d * (j - C0 - (R-1)/2)
			#~ print A[i][j],
		#~ print ""
	mi /= R
	mj /= C
	#~ print mi,mj
	return abs(mi) < 1e-5 and abs(mj) < 1e-5


def incerc(R,C,D,A):
	sol = "IMPOSSIBLE"
	for r in range(min(R,C), 2, -1):
		for i in range(R - r + 1):
			for j in range(C - r + 1):
				#~ print i,j,r
				if check(i,j,r,D):
					sol = r
					return sol
	return sol

for kkk in range(T):
	R,C,D = readlist()
	A = []
	for i in range(R):
		A.append([int(c) for c in sys.stdin.readline().strip()])
	
	sol = incerc(R,C,D,A)
	
	print "Case #%d: %s" % (kkk+1, sol)
