import math, itertools
for tc in xrange(input()):
	n, k = map(int, raw_input().split())
	a = []
	for c in xrange(n):
		a.append(map(int, raw_input().split()))
	a.sort(key=lambda x: [-x[0]])
	a = map(lambda x: (math.pi * x[0] * x[0], 2 * math.pi * x[0] * x[1]), a)
	comb = itertools.combinations(a, k)
	area = 0.0
	for i in comb:
		h = 0.0
		for j in i:
			h += j[1]
		area = max(area, i[0][0]+h)
	print 'Case #{0}: {1}'.format(tc+1, area)
