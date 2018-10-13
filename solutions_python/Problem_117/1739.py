
def canDoLine(X, i, M, h):
	'''
	can do line if the line only contains <= h and at least one place with value h
	0: do not do, 1, do, -1 pb impossible

	'''
	found = False
	for j in xrange(M):
		if X[i][j] > h: return 0
		if X[i][j] < h and X[i][j] > -1: return -1
	return 1

def canDoCol(X, N, j, h):
	found = False
	for i in xrange(N):
		if X[i][j] > h: return False
		if X[i][j] == h: found = True
	return found

def possible(X, N, M):

	for h in xrange(1,101):

		for i in xrange(N):
			# line i
			res = canDoLine(X, i, M, h)
			if res == -1: return False
			if res == 1:
				for j in xrange(M): X[i][j] = -1

		for j in xrange(M):
			res = canDoCol(X, N, j, h)
			if res == -1: return False
			if res == 1:
				for i in xrange(N): X[i][j] = -1

	for i in xrange(N):
		for j in xrange(M):
			if X[i][j] != -1: return False 
	return True


file = open("input.txt")

T = int(file.next())

for t in xrange(T):

	N, M = map(int, file.next().split())
	X = [ map(int, file.next().split()) for i in xrange(N) ]

	if possible(X, N, M): print "Case #%d: YES" % (t+1)
	else: print "Case #%d: NO" % (t+1)

