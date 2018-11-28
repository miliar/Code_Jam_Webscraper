def isKit(reqs, ings):
    curr_low, curr_high = None,None

    for req, ing in zip(reqs, ings):
        low = req*0.9
        high = req*1.1
        k_low = ing/low
        k_high = ing/high
        if curr_high == None:
            curr_high = k_high
            curr_low = k_low
        else:
            curr_low = min(curr_low, k_low)
            curr_high = max(curr_high, k_high)
    return int(curr_low) >= curr_high and int(curr_low) > 0

# Hopcroft-Karp bipartite max-cardinality matching and max independent set
# David Eppstein, UC Irvine, 27 Apr 2002
# from http://code.activestate.com/recipes/123641-hopcroft-karp-bipartite-matching/

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
    

def solve():
    N, P = raw_input().split()
    N = int(N)
    P = int(P)
    req = map(int, raw_input().split())
    ingred = [] 
    for i in range(N):
        l = raw_input()
        l = map(int, l.split())
        ingred.append(l)

    if N == 1:
        kits = 0
        low = req[0]*0.9
        high = req[0]*1.1
        for ing in ingred[0]:
            if isKit(req, [ing]):
                kits += 1
        return kits
    elif N == 2:
        # create edges
        ns = {}
        for i in range(P):
            if i not in ns:
                ns[i] = []
            for j in range(P):
                if isKit(req, [ingred[0][i], ingred[1][j]]):
                    ns[i].append(j)
        a, _, _ =  bipartiteMatch(ns)
            

        return len(a)
    else:
        return 'ERROR'
        


if __name__ == '__main__':
    T = int(raw_input())
    for i in range(1, T+1):
        print "Case #{}: {}".format(i, solve())
