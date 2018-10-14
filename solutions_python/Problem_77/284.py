from __future__ import division
import sys, string
import itertools
import math

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

def key(element):
    return element

def find_cycles(l):
    seen = set()
    cycles = []
    for i in range(len(l)):
        if i != key(l[i]) and not i in seen:
            cycle = []
            n = i
            while 1: 
                cycle.append(n)
                n = key(l[n])
                if n == i:
                    break
            seen = seen.union(set(cycle))
            cycles.append(list(reversed(cycle)))
    return cycles

cL = {}
cP = {}
def P(n,k): # prob sa pice i bune din n (nu mai multe)
	try:
		L = cL[n]
	except:
		L = list(itertools.permutations(range(n)))
		cL[n] = L
	
	if (n,k) in cP:
		return cP[n,k]

	print >> sys.stderr, "P(%d,%d)" % (n,k)

	S = [ sum([1 if i==x else 0 for i,x in enumerate(a)]) for a in L ]
	ans = len(filter(lambda x:x==k, S)) / float(len(L))
	cP[n,k] = ans
	return ans

cQ = {}
def Q(n): # cat timp imi trebuie
	if n < 1: return 0
	if n == 1: return 0
	if n == 2: return 2

	if n in cQ:
		return cQ[n]

	print >> sys.stderr, "Q(%d)" % n

	r = 1
	for i in range(1,n+1):
		r += P(n,i) * Q(n-i)
	q = r / (1 - P(n,0))
	
	cQ[n] = q
	return q

for t in range(T):
	N = int(sys.stdin.readline())
	print >> sys.stderr, t, N
	L = readlist()
	S = list(L)
	S.sort()
	p = [S.index(x) for x in L]
	#~ print p
	C = find_cycles(p)
	#~ print C
	g = 0
	s = 0
	for c in C:
		s += len(c)
		#~ print len(c)
	g = Q(s)
	ans = "%.10f" % g
	print "Case #%d: %s" % (t+1, ans)
