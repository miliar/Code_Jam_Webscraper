import sys
import math
import itertools

f = open(sys.argv[1], 'r')
cases = int(f.readline())
for case in xrange(cases):
	r,k,g_num = map(int,f.readline().split())
	g = map(int,f.readline().split())
	money = 0
	for round in xrange(r):
		current_k = k
		g2 = []
		while g:
			current_g = g[0]
			if current_k - current_g >= 0:
				current_k = current_k - current_g
				g.pop(0)
				g2.append(current_g)
				money = money + current_g
			else:
				break
		g = g + g2
	print 'Case #%d: %d' % (case+1,money)