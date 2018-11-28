import sys

fin = sys.stdin

C = int (fin.readline())

for c in xrange(1, C+1):
    R = int(fin.readline())
    bac = set([]) # use (X, Y) for coordinates
    
    for r in xrange(R):
	X1, Y1, X2, Y2 = map(int, fin.readline().split())
	for x in xrange(X1, X2+1):
	    for y in xrange(Y1,Y2+1):
		bac.add( (x, y) )
	
    t = 0
    while len(bac) > 0:
	#print bac
	t += 1
	dead = []
	born = []
	for b in bac:
	    # check if die
	    nn = (b[0], b[1] - 1)
	    wn = (b[0] - 1, b[1])
	    
	    inter = bac.intersection(set([nn, wn]))
	    if len(inter) == 0:
		dead.append(b)
	
	    # check if has down left neighbour for newborn
	    swn = (b[0] - 1, b[1] + 1)
	    inter = bac.intersection(set([swn]))
	    if len(inter) == 1:
		born.append((b[0], b[1] + 1))
		
	#print dead
	#print born
	for a in dead:
	    bac.remove(a)
	
	for a in born:
	    bac.add(a)
    print 'Case #' + str(c) + ":", t
	
    
