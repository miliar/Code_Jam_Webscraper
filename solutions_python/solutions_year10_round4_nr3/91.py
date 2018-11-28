import sys

def pairs(P):
	r = set()
	for p in P:
		if (p[0]+1, p[1]-1) in P:
			r.add(p)
	return r

def lone(P):
	r = set()
	for p in P:
		if (p[0]-1, p[1]) not in P and (p[0], p[1]-1) not in P:
			r.add(p)
	return r

def step(P, op, lp):
	newop = set()
	delp = set()
	for p in op:
		newp = p[0]+1, p[1] 
		if newp not in P:
			P.add(newp)
			if (newp[0]+1, newp[1]-1) in P:
				newop.add(newp)
			xp = (newp[0]-1, newp[1]+1) 
			if xp in P:
				newop.add(xp)
			xp = (newp[0]+1, newp[1])
			if xp in lp:
				delp.add(xp)
			xp = (newp[0], newp[1]+1)
			if xp in lp:
				delp.add(xp)
	newlp = set()
	for p in lp:
		P.remove(p)
		if p in op:
			op.remove(p)
		xp = (p[0]-1, p[1]+1) 
		if xp in op:
			op.remove(xp)
		alp = (p[0]+1, p[1])
		if alp in P and (alp[0], alp[1]-1) not in P: 
			newlp.add(alp)
		alp = (p[0], p[1]+1)
		if alp in P and (alp[0]-1, alp[1]) not in P: 
			newlp.add(alp)
	return P, op | newop, newlp

C=int(sys.stdin.readline())
for case in range(C):
	P = set()
	R = int(sys.stdin.readline())
	for r in range(R):
		(X1,Y1,X2,Y2) = map(int, sys.stdin.readline().split())
		for x in range(X2-X1+1):
			for y in range(Y2-Y1+1):
				P.add((X1+x,Y1+y))
		op = pairs(P)
		lp = lone(P)
	steps = 0
	while len(P) > 0:
#		print P, op, lp
		P, op, lp = step(P, op, lp)
		steps += 1
		
	print "Case #%d: %d" % (case+1, steps)