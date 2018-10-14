#############################################################################
#                           IMPORTS AND GLOBALS                             #
#############################################################################

from gcj_io import *
import pdb

#############################################################################
#                           PROBLEM SPECIFIC CODE                           #
#############################################################################

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def solve_rec(Sr, K, M, ssf):
	if Sr == 0:
		x = occurrences(ssf, M)
		return (1,x, x) 
	else:
		bestsf = 0
		totsf = 0
		nsf = 0
		for i in xrange(len(K)):
			res = solve_rec(Sr-1, K, M, ssf+K[i])
			nsf += res[0]
			totsf += res[1]
			bestsf = max(res[2], bestsf)
		return (nsf, totsf, bestsf)		

def solve_small(S, K, M):
	nsf, totsf, bestsf = solve_rec(S, K, M, "")
	ret = bestsf - float(totsf)/nsf
	return ret

def solve_large(V):
	return 0
			
def solve_case(S, K, M):
	print S, K, M
	return solve_small(int(S), K, M)
	
		
	
#############################################################################
#                           SOLUTION CODE                                   #
#############################################################################

def solve(fin, fout):
	f = open(fin,'rt')
	X = [t.strip() for t in f.readlines()]
	f.close()
	S = [t.split()[2] for t in X[1:len(X):3]]		
	K = [t for t in X[2:len(X):3]]
	M = [t for t in X[3:len(X):3]]
	output = []
	for i in xrange(len(S)):
		output.append(solve_case(S[i], K[i], M[i]))
	gcj_write_simple(fout, output)



#############################################################################
#                           CALL-ON-RUNNING                                 #
#############################################################################

#sys.setrecursionlimit(1010)	
#solve('B-test.in', 'B-test.out')	
solve('B-small-attempt0.in', 'B-small-attempt0.out')
#solve('B-small-attempt1.in', 'B-small-attempt1.out')
#solve('B-small-attempt2.in', 'B-small-attempt2.out')
#solve('B-small-attempt3.in', 'B-small-attempt3.out')
#solve('B-small-attempt4.in', 'B-small-attempt4.out')
#solve('B-large.in', 'B-large.out')
