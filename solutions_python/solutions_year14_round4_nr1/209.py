#############################################################################
#                           IMPORTS AND GLOBALS                             #
#############################################################################
from bisect import bisect_right

#############################################################################
#                           BASIC INPUT/OUTPUT CODE                         #
#############################################################################

# Quick read if the data is one-per-line integers
def gcj_read_simple(fname, fMap=int):
	f = open(fname, 'rt')
	return [map(fMap, x.strip().split()) for x in f.readlines()[1:]]		
	f.close()

# One-per-twoline with first line removable	
def gcj_read_simple_2(fname, fMap=int):
	f = open(fname, 'rt')
	return [map(fMap, x.strip().split()) for x in f.readlines()[2:-1:2]]
	f.close()

# Quick read T groups of N lines each (N given a line before as first element)
def gcj_read_N(fname, Nelt = 0, fMap=str, fOfN = lambda x: x):
	f = open(fname, 'rt')
	L = [x.strip().split() for x in f.readlines()]
	f.close()
	T = int(L[0][0])
	output = []
	ln = 1
	for i in xrange(T):
		N = fOfN(int(L[ln][Nelt]))
		output.append([map(fMap, x) for x in L[ln+1:ln+N+1]])
		ln += (N+1)			
	return output
	
# Quick read T groups of lines given by some function of the first line among them
# Exact same default behaviour as gcj_read_N; but more flexible
def gcj_read_f(fname, fMapFn=lambda x: [str]*x[0], fOfN = lambda x: x[0]):
	f = open(fname, 'rt')
	L = [x.strip().split() for x in f.readlines()]
	f.close()
	T = int(L[0][0])
	output = []
	ln = 1
	for i in xrange(T):
		N = fOfN(map(int,L[ln]))
		fMap = fMapFn(map(int,L[ln]))
		output.append([map(fMap[k], L[ln+1+k]) for k in xrange(N)])
		ln += (N+1)			
	return output
# e.g. L = gcj_read_f('C-test.in', lambda x: [str]*x[0] + [int]*x[1], lambda x: x[0]+x[1])

# GCJ_READ_F with multi-line headers (also saves the headers if storeHead=True)
# This is the most general read function and can mimic (almost) the behaviour of all the others
def gcj_read_f_multi(fname, nlines_head=1,fMapFn=lambda x: [str]*x[0][0], fOfN = lambda x: x[0][0], storeHead=True):
	f = open(fname, 'rt')
	L = [x.strip().split() for x in f.readlines()]
	f.close()
	T = int(L[0][0])
	output = []
	ln = 1
	for i in xrange(T):
		head = [map(int, x) for x in L[ln:ln+nlines_head]]
		N = fOfN(head)
		fMap = fMapFn(head)
		if storeHead:
			output.append([head,[map(fMap[k], L[ln+nlines_head+k]) for k in xrange(N)]])
		else:
			output.append([map(fMap[k], L[ln+nlines_head+k]) for k in xrange(N)])
		ln += (N+nlines_head)
	return output

	
def gcj_read_fixed(fname, N, fMaps):
	f = open(fname, 'rt')
	L = [x.strip().split() for x in f.readlines()]
	f.close()
	T = int(L[0][0])
	ln = 1
	output = []
	for i in xrange(T):
		output.append([map(fMaps[k], L[ln+k]) for k in xrange(N)])
		ln+=N
	return output
	
# Quick one-item-per-line outputs	
def gcj_write_simple(fname, lst):
	f = open(fname, 'wt')
	f.writelines(['Case #' + str(i+1) + ': ' + str(lst[i]) + '\n' for i in xrange(len(lst))])	
	f.close()
	return

# Write a list of lists of strings
def gcj_write_slst(fname, strlst):
	lwrt = []
	for i in xrange(len(strlst)):
		lwrt.append(['Case #' + str(i+1) + ':'])
		lwrt.extend(map(lambda x: str(x) + '\n'), strlst[i])
		
	f = open(fname, 'wt')
	f.writelines(lwrt)
	f.close()
	return


#############################################################################
#                           PROBLEM SPECIFIC CODE                           #
#############################################################################

def solve_case(V):
	X = V[0][1]
	S = V[1]
	S.sort()
	numDisks = 0
	while(len(S)>0):
		numDisks+=1
		limit = X-S[-1]
		del(S[-1])		
		if(len(S)==0):
			break
		nextElt = bisect_right(S, limit)-1
		if(nextElt>=len(S)):
			nextElt = len(S)-1
		if(nextElt<0):
			nextElt = 0
		if S[nextElt] <= limit:
			del(S[nextElt])
		
	return numDisks
	
#############################################################################
#                           SOLUTION CODE                                   #
#############################################################################

def solve(fin, fout):
	data = gcj_read_fixed(fin, 2, [int, int])
	output = map(solve_case, data)
	gcj_write_simple(fout, output)



#############################################################################
#                           CALL-ON-RUNNING                                 #
#############################################################################

#sys.setrecursionlimit(1010)	
#solve('A-test.in', 'A-test.out')	
#solve('A-small-attempt0.in', 'A-small-attempt0.out')
#solve('A-small-attempt1.in', 'A-small-attempt1.out')
#solve('A-small-attempt2.in', 'A-small-attempt2.out')
#solve('A-small-attempt3.in', 'A-small-attempt3.out')
#solve('A-small-attempt4.in', 'A-small-attempt4.out')
solve('A-large.in', 'A-large.out')