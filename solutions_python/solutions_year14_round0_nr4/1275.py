import os, sys
import itertools
lines = [line.strip() for line in open("%s" % sys.argv[1]).readlines()]
lines.reverse()
cases = lines.pop()
for case in range(int(cases)):
	lines.pop()
	lowers, highers = [], []
	N = sorted(map(float,lines.pop().split(' ')))
	K = sorted(map(float,lines.pop().split(' ')))
	for i, n in enumerate(N):
		try:
			lower = max(filter(lambda x: x<n and x not in lowers, K))
			lowers.append(lower)
		except:
			lower = None
		try:
			higher = max(filter(lambda x: x>n and x not in highers, K))
			highers.append(higher)
		except:
			higher = None
	print "Case #%s:" % (case+1),
	print len(lowers),
	print len(filter(lambda x: x[0] >x[1], [(n,K.pop(K.index(min(filter(lambda x: x>n, K) or K)))) for n in N]))