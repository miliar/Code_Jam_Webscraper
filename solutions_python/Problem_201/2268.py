def solveForOne(N):
	N = int(N)
	if (N%2==0):
		Ls = (N/2) - 1
		Rs = N/2
	else:
		Ls = N/2
		Rs = N/2
	return Ls, Rs

def iterateProblemAndSolve(N, K):
	# Setup
	N = int(N)
	K = int(K-1)
	p = {}
	keys = []
	currkey = 0
	newkey = 0
	# Insert first problem
	p[N] = 1
	keys.append(N)

	for i in xrange(K):
		currkey = keys[0]
		p[currkey] = p[currkey] - 1
		newkey = currkey/2
		if newkey not in p:
			p[newkey] = 0
			keys.append(newkey)
		p[newkey] = p[newkey] + 1
		if (currkey%2==0):
			newkey = newkey - 1
			if newkey not in p:
				p[newkey] = 0
				keys.append(newkey)
			p[newkey] = p[newkey] + 1
		else:
			p[newkey] = p[newkey] + 1
		#clean if no more cases
		if p[currkey] == 0:
			keys.pop(0)
			del p[currkey]

	return solveForOne(keys[0])

t = int(raw_input())
for i in xrange(1, t + 1):
	n, k = [int(s) for s in raw_input().split(" ")]
	l,r = iterateProblemAndSolve(n, k)
	print "Case #{}: {} {}".format(i, r, l)
