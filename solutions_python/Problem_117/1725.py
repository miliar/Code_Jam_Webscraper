import sys, os, itertools

def checkLawn(lawn,n,m):
	for i in range(n):
		for j in range(m):
			if lawn[i][j] != max(lawn[i]):
				not_found.append((j,i))
	if not_found:
		lawn = zip(*lawn)
		for i,j in not_found:
			if lawn[i][j] != max(lawn[i]):
				return "NO"
	return "YES"
	
fi = sys.stdin
lawns = []
T = int(fi.readline())
for case in range(T):
	this_lawn = []
	not_found = []
	N,M = map(int,fi.readline()[:-1].split(' '))
	for i in range(N):
		this_lawn.append(fi.readline()[:-1].split(' '))
	print "Case #%s: %s" % (case+1,checkLawn(this_lawn,N,M))

		
