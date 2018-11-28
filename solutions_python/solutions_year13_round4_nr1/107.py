#!/usr/bin/env python

def read_ints():
	return map(int, raw_input().strip().split())

T, = read_ints()

def dictadd(d, k, v):
	if k in d:
		d[k] += v
	else:
		d[k] = v

def cost(a, b):	
	k = b-a
	return ((2*n-k+1)*k)/2

for cur_test in xrange(1, T+1):
	n, m = read_ints()

	lin, lout = dict(), dict()

	GOODCOST = 0

	for x in range(m):
		u, v, c = read_ints()
		dictadd(lin, u, c)
		dictadd(lout, v, c)

		GOODCOST += cost(u,v) * c
		
	stack = []

	MINCOST = 0

	for s in xrange(1, n+1):
		if s in lin:
			stack.append((s, lin[s]))
		if s in lout:			
			x = lout[s]

			while x>0:
				pn = min(stack[-1][1], x)
				st = stack[-1][0]
				x -= pn

				if stack[-1][1] == pn:
					del stack[-1]
				else:
					stack[-1] = (st, stack[-1][1]-pn)


				MINCOST += cost(st, s) * pn
			

	res = GOODCOST - MINCOST
	print 'Case #{}: {}'.format(cur_test, res)
