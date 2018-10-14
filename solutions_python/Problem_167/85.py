#############################################################################
#                           IMPORTS AND GLOBALS                             #
#############################################################################

from gcj_io import *


#############################################################################
#                           PROBLEM SPECIFIC CODE                           #
#############################################################################


def solve_greedy(C, V, W):
	T = [0]*(V+1)
	T[0] = 1
	for w in W:
		for c in xrange(C):
			for t in xrange(V, w-1, -1):
				T[t] = max(T[t], T[t-w])
	
	ret = 0
	for w in xrange(1,V+1):
		if T[w] == 0:
			ret += 1
			for c in xrange(C):
				for t in xrange(V, w-1, -1):
					T[t] = max(T[t], T[t-w])
	return ret
				
			
def solve_case(CDV, W):
	C, D, V = CDV
	print C, D, V, ":", W
	return solve_greedy(C, V, W)

#############################################################################
#                           SOLUTION CODE                                   #
#############################################################################

def solve(fin, fout):
	f = open(fin, 'rt')
	X = [map(int, t.strip().split()) for t in f.readlines()]
	f.close()
	CDV = X[1:len(X):2]
	vals = X[2:len(X):2]
	output = []
	for i in xrange(len(CDV)):
		output.append(solve_case(CDV[i], vals[i]))
	gcj_write_simple(fout, output)



#############################################################################
#                           CALL-ON-RUNNING                                 #
#############################################################################

#sys.setrecursionlimit(1010)	
#solve('C-test.in', 'C-test.out')	
solve('C-small-attempt0.in', 'C-small-attempt0.out')
#solve('C-small-attempt1.in', 'C-small-attempt1.out')
#solve('C-small-attempt2.in', 'C-small-attempt2.out')
#solve('C-small-attempt3.in', 'C-small-attempt3.out')
#solve('C-small-attempt4.in', 'C-small-attempt4.out')
#solve('C-large.in', 'C-large.out')