from math import *

filename = 'B-large'
fin = open('%s.in' % filename)
fout = open('%s.out' % filename, 'w')

cases = int(fin.readline().strip())
for case in xrange(cases):
	C, D = [int(x) for x in fin.readline().strip().split()]
	P = [0] * C
	cost = [0] * C
	g = []
	ans = 0
	for i in xrange(C):
		P[i], V = [int(x) for x in fin.readline().strip().split()]
		cost[i] = 0.5 * D * (V - 1)
		ans = max(ans, cost[i])
		g.append([0] * C)
	for i in xrange(C):
		for j in xrange(i+1, C):
			L = D * (j - i)
			for k in xrange(i, j+1):
				L += cost[k]*2
			L -= (cost[i]+cost[j])
			if (P[j] - P[i] >= L):
				continue
			else:
				ans = max(ans, (L - (P[j] - P[i]) + cost[i] + cost[j])/2)
	print 'Case #%d:' % (case+1), ans

fin.close()
fout.close()
