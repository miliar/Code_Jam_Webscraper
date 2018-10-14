from itertools import *
import math

infile = "D-small-attempt3.in"

lines = [s.rstrip() for s in open(infile, "rb").readlines()]
NCases=int(lines[0])

def C(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
#math.factorial(x)

def D(n, k):
    if (k == 0):
        if (n == 0):
            return 1
        else:
            return round(math.factorial(n) / math.e)
    return C(n, k) * D(n - k, 0)

def meantime(n):
    if (n == 0 or n == 1):
        return (n)
    perm = math.factorial(n) * 1.0
    nnull = D(n, 0) 

    atleast1 = 1 - (D(n, 0) / perm)
    #print "atleast1",atleast1
    timeatleast1 = 1/atleast1
    #print timeatleast1
    #print "p", [D(n, k+1) / perm for k in range(n)]
    #print "M", [meantime(n-(k+1)) for k in range(n)]
    #permnonz = math.factorial(n-1) * 1.0
    res = [D(n, k+1) / (perm - nnull) * meantime(n-(k+1) ) for k in range(n)]
    #print "res", res, sum(res) + atleast1
    #print "res", [D(n, k+1) / perm for k in range(n-1)]
    result = sum(res) + timeatleast1
    #print ("meantime, %d=%d" % (n,result))
    return (result)
	
    #return C(n, k) * D(n - k, 0)
	

def findcycle(elms, idx):
	start = idx = elms[idx-1]
	#print "--start=%d" % (start)
	visited = set([start])
	while (elms[idx-1] not in visited):
		#print "----visit:" + str(elms[idx-1])
		idx = elms[idx-1]
		visited.add (idx)
		if elms[idx-1] == start:
			return (visited)
	return (None)

for i in range(NCases):
	values = [int(c) for c in lines[i * 2 + 2].split(" ")]
	cycles = set()
	for j, v in enumerate(values):
		cy = findcycle(values, j+1)
		if cy != None:
			cycles.add(frozenset(cy))
	#print "values:", values
	#print cycles
	result = sum([meantime(len(c)) for c in cycles]) * 1.0
	#print result
	print "Case #%d: %.8f" % (i+1, result)

	
	
	
	