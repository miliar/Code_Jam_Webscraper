#!/usr/bin/python


def readints(fd):
	return [ int(x) for x in fd.readline().strip().split() ]


def tarzan(D, I, dist):
	KNOWN = dict()
	return tarzanD(KNOWN, D, I, dist, (0, D[0]))

def tarzanD(KNOWN, D, I, dist, prev):
	
	b, r = prev
	c = D[b]
	if c+r>=dist:
		return True
	
	# Select the candidates
	for i in range(b+1, len(D)):
		delta = D[i]-c
		if delta>r:
			break
		nxt = (i, min(delta, I[i]))
		if nxt in KNOWN:
			v = KNOWN[nxt]
		else:
			v = tarzanD(KNOWN, D, I, dist, nxt)
			KNOWN[nxt] = v
		if v:
			return True
	return False


def solve(fd):
	T = readints(fd)[0]
	
	for i in range(T):
		# Read
		N = readints(fd)[0]
		D = [0]*N
		I = [0]*N
		for j in range(N):
			D[j], I[j] = readints(fd)
		dist = readints(fd)[0]
		
		res = tarzan(D, I, dist)
		if res:
			print("Case #%d: YES" % (i+1))
		else:
			print("Case #%d: NO" % (i+1))



import sys

if len(sys.argv)<2:
	print("Too few args")
else:
	fd = open(sys.argv[1], "r")
	solve(fd)
	fd.close()

