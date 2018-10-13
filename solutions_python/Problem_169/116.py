import fileinput
stdin = fileinput.input()

eps = 10e-10

def solveCase():
	N,V,X = stdin.next().split()
	N = int(N)
	V = float(V)
	X = float(X)
	S = [map(float,stdin.next().split()) for s in xrange(N)]
	sorted(S,key=lambda (v,x):v/x)
	Vi = [v for v,x in S]
	Xi = [x for v,x in S]

	hax = "IMPOSSIBLE"
	t = sum(v for v,x in S if x==X)
	if t>0:
		hax = V/t

	totV = sum(Vi)
	totX = sum(v*x for v,x in S)/totV
	cV = totV
	cX = totX
	if totX<X:
		# must heat
		# turn off S[0..]
		for sV,sX in S[::-1]:
			if sX<=X:
				if abs(X*sV-sX*sV)>eps:
					a = (X*cV-cX*cV)/(X*sV-sX*sV)
					if 0<=a<1-eps:
						return V/(cV-a*sV)
					if cV==sV:
						return hax
					cX = (cX*cV-sX*sV)/(cV-sV)
					cV -= sV
		return hax
	if totX>X:
		# must heat
		# turn on S[..|S|-1]
		for sV,sX in S[::-1]:
			if sX>=X:
				if abs(X*sV-sX*sV)>eps:
					a = (X*cV-cX*cV)/(X*sV-sX*sV)
					if 0<=a<1-eps:
						return V/(cV-a*sV)
					if cV==sV:
						return hax
					cX = (cX*cV-sX*sV)/(cV-sV)
					cV -= sV
		return hax
	return V/cV

for case in xrange(int(stdin.next())):
	print "Case #{0}: {1}".format(case+1,solveCase())