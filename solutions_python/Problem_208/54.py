T = int(raw_input())

def doprob():
	N, Q = map(int, raw_input().split())
	E = []
	S = []
	for i in xrange(N):
		e, s = map(int, raw_input().split())
		E.append(e)
		S.append(s)
	G = {}
	for i in xrange(N):
		G[i] = map(int, raw_input().split())
	q = []
	for i in xrange(Q):
		s, e = map(int, raw_input().split())
		q.append([s-1,e-1])

	# Floyd Warshall
	distances = {}
	for i in xrange(N):
		distances[i] = list(G[i])
		distances[i][i] = 0
	for k in xrange(N):
		for i in xrange(N):
			for j in xrange(N):
				if distances[i][k] < 0 or distances[k][j] < 0:
					continue
				if distances[i][j] < 0:
					distances[i][j] = distances[i][k] + distances[k][j]
				if distances[i][j] > distances[i][k] + distances[k][j]:
					distances[i][j] = distances[i][k] + distances[k][j]
#	print distances
	out = ""
	for start, end in q:
		times = [None] * N
		times[start] = 0
		for i in xrange(N):
			newtimes = [None] * N
			for j in xrange(N):
				if times[j] == None:
					continue
				for k in xrange(N):
#					print "asdf", distances[j][k], E[j], S[j]
					if distances[j][k] < 0 or distances[j][k] > E[j]:
						continue
					if times[k] == None:
						times[k] = times[j] + distances[j][k]*1.0/S[j]
					elif times[k] > times[j] + distances[j][k]*1.0/S[j]:
						times[k] = times[j] + distances[j][k]*1.0/S[j]
					else:
						times[k] = times[k]
#					print "tem ", times[j] + distances[j][k]*1.0/S[j] 
#			times = newtimes
#			print newtimes
		out += str(times[end]) + " "
	return out

"""	D = {N-1: 0}
	for i in xrange(N-1):
		D[i] = None
	for i in reversed(xrange(N-1)):
		score = None
		for j in reversed(xrange(i+1, N)):
			if dists[j]-dists[i] <= E[i] and D[j] != None:
				if D[i] == None:
					D[i] = (dists[j]-dists[i])*1.0/S[i] + D[j]
				elif (dists[j]-dists[i])*1.0/S[i] + D[j] < D[i]:
					D[i] = (dists[j]-dists[i])*1.0/S[i] + D[j]
	return D[0]"""


for qq in xrange(T):
	print "Case #" + str(qq+1) + ": " + str(doprob())