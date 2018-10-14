import sys

f = open(sys.argv[1])
T = int(f.readline())

def check(lawn, N, M):
	maxR, maxC = [0] * N, [0] * M
	for i, row in enumerate(lawn):
		for j, v in enumerate(row):
			if maxR[i] < v:
				maxR[i] = v
			if maxC[j] < v:
				maxC[j] = v
	
	for i, row in enumerate(lawn):
		for j, v in enumerate(row):
			if v < maxR[i] and v < maxC[j]:
				return "NO"
	return "YES"

for t in xrange(1, T+1):
	N, M = map(int, f.readline().split())
	lawn = [map(int, f.readline().split()) for n in xrange(N)]
	print "Case #{0}: {1}".format(t, check(lawn, N, M))

