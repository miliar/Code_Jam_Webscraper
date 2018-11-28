import sys
from collections import deque

def mainCase(valA,valB):
	R,K,NS = map(int,valA.rstrip().split(" "))
	N = deque(map(int,valB.rstrip().split(" ")))
	O = deque()
	
	result = 0
	
	for i in xrange(R):
		T = 0
		while (len(N)>0) and (T + N[0]) <= K:
			L = N.popleft()
			O.append(L)
			T += L
			result += L
		N.extend(O)
		O = deque()

	return str(result)
	
	
fname = "/Users/fopina/Downloads/C-small-attempt0.in"
#fname = "t.in"

f = open(fname,"r")
tnr = int(f.readline())

for i in xrange(1,tnr+1):
	print "Case #" + str(i) + ": " + mainCase(f.readline(),f.readline())
