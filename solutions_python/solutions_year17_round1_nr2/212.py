# Hopcroft-Karp bipartite max-cardinality matching and max independent set
# David Eppstein, UC Irvine, 27 Apr 2002


def bipartiteMatch(graph):
	'''Find maximum cardinality matching of a bipartite graph (U,V,E).
	The input format is a dictionary mapping members of U to a list
	of their neighbors in V.  The output is a triple (M,A,B) where M is a
	dictionary mapping members of V to their matches in U, A is the part
	of the maximum independent set in U, and B is the part of the MIS in V.
	The same object may occur in both U and V, and is treated as two
	distinct vertices if this happens.'''
	
	# initialize greedy matching (redundant, but faster than full search)
	matching = {}
	for u in graph:
		for v in graph[u]:
			if v not in matching:
				matching[v] = u
				break
	
	while 1:
		# structure residual graph into layers
		# pred[u] gives the neighbor in the previous layer for u in U
		# preds[v] gives a list of neighbors in the previous layer for v in V
		# unmatched gives a list of unmatched vertices in final layer of V,
		# and is also used as a flag value for pred[u] when u is in the first layer
		preds = {}
		unmatched = []
		pred = dict([(u,unmatched) for u in graph])
		for v in matching:
			del pred[matching[v]]
		layer = list(pred)
		
		# repeatedly extend layering structure by another pair of layers
		while layer and not unmatched:
			newLayer = {}
			for u in layer:
				for v in graph[u]:
					if v not in preds:
						newLayer.setdefault(v,[]).append(u)
			layer = []
			for v in newLayer:
				preds[v] = newLayer[v]
				if v in matching:
					layer.append(matching[v])
					pred[matching[v]] = v
				else:
					unmatched.append(v)
		
		# did we finish layering without finding any alternating paths?
		if not unmatched:
			unlayered = {}
			for u in graph:
				for v in graph[u]:
					if v not in preds:
						unlayered[v] = None
			return (matching,list(pred),list(unlayered))

		# recursively search backward through layers to find alternating paths
		# recursion returns true if found path, false otherwise
		def recurse(v):
			if v in preds:
				L = preds[v]
				del preds[v]
				for u in L:
					if u in pred:
						pu = pred[u]
						del pred[u]
						if pu is unmatched or recurse(pu):
							matching[v] = u
							return 1
			return 0

		for v in unmatched: recurse(v)

from sys import stdin
readline = stdin.readline
import math

def lohi(Q, R):
	lo = math.ceil(Q/(1.1*R))
	hi = math.floor(Q/(0.9*R))
	
	if hi < lo:
		return False
	else:
		return (lo, hi)

T = int(readline())
for t in xrange(1, T+1):
	N, P = map(int, readline().strip().split())
	R = map(int, readline().strip().split())
	
	Q = []
	for i in xrange(N):
		Q.append(map(int, readline().strip().split()))
	
	for i in xrange(N):
		for j in xrange(P):
			lohi_ = lohi(Q[i][j], R[i])
			if lohi_ != False:
				Q[i][j] = (j, lohi_[0], lohi_[1])
			else:
				Q[i][j] = False
	
	if N == 1:
		ans = 0
		for j in xrange(P):
			if Q[0][j] != False:
				ans += 1
		
		print "Case #%d: %d" % (t, ans)
		continue
	
	if N == 2:
		U = [x for x in Q[0] if x != False]
		V = [x for x in Q[1] if x != False]
		
		graph = {}
		for u in U:
			graph[u[0]] = []
			for v in V:
				if max(u[1], v[1]) <= min(u[2], v[2]):
					graph[u[0]].append(v[0])
		
		print "Case #%d: %d" % (t, len(bipartiteMatch(graph)[0]))
