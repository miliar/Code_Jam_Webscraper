n = int(raw_input())

def evaltree(tree,pos):
	l = tree[pos]
	
	c = l[1]
	g = l[0]
	
	if l[0] == None:
		val = l[2]
		
		if val == 0:
			return (0,999999999)
		else:
			return (999999999,0)
	
	cl = evaltree(tree,(2*pos))
	cr = evaltree(tree,(2*pos)+1)
	
	costAnd0 = min(cl[0] + cr[1],cl[0] + cr[0],cl[1] + cr[0])
	costAnd1 = cl[1] + cr[1]
	
	costOr1 = min(cl[0] + cr[1],cl[1] + cr[1],cl[1] + cr[0])
	costOr0 = cl[0] + cr[0]
	
	if g == 0 and c == 1:
		cost1 = min(costOr1,costAnd1 + 1)
		cost0 = min(costOr0,costAnd0 + 1)
	elif g==0 and c==0:
		cost1 = costOr1
		cost0 = costOr0
	if g == 1 and c == 1:
		cost1 = min(costOr1+1,costAnd1 )
		cost0 = min(costOr0+1,costAnd0 )
	elif g==1 and c==0:
		cost1 = costAnd1
		cost0 = costAnd0
	#print pos, (cost0, cost1)
	return (cost0,cost1)
		


for case in xrange(1,n+1):
	(m,v) = tuple(int(j) for j in raw_input().split())
	
	tree = [[None,None,None] for i in xrange(m+1)]
	
	#print (m-1)/2, (m+1)/2
	
	for i in xrange(0,(m-1)/2):
		g,c = tuple(int(j) for j in raw_input().split())
		
		tree[i+1][0] = g
		tree[i+1][1] = c
	for i in xrange(0,(m+1)/2):
		p = int(raw_input())
		tree[((m-1)/2) + i+1][2] = p
	#print tree
	
	mincosts = evaltree(tree,1)
	#print mincosts
	if mincosts[v] > 100000:
		print "Case #%d: IMPOSSIBLE" % case
	else:
		
		print "Case #%d: %d" % (case,mincosts[v])
	
		