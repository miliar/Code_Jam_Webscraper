from math import pi

def solve(n, k, pancakes):
	res = 0
	taken = [0 for _ in xrange(n)]
	heights = [2*pi*p[0]*p[1] for p in pancakes]
	maxsurf = 0
	index = 0
	for i in xrange(k - 1):
		maxx = -1
		for j in xrange(n):
			if heights[j] > maxx and taken[j] == 0:
				maxx = heights[j]
				index = j
		res += maxx
		taken[index] = 1
		if maxsurf < pancakes[index][0]:
			maxsurf = pancakes[index][0]
	#print heights
	#print maxsurf, 'u', res
	res += pi*maxsurf*maxsurf

	
	best = -1
	for i in xrange(n):
		val = -10
		if taken[i] == 0:
			lateral = 2*pi*pancakes[i][0]*pancakes[i][1]
			top = pi*pancakes[i][0]*pancakes[i][0]
			if pancakes[i][0] > maxsurf:
				val =  lateral + top - pi*maxsurf*maxsurf
			else:
				val = lateral
			if val > best:
				best = val
				
	#print 2*pi*8*4, 'y'

	res += best
	return res

print solve(2, 1, [(100,20), (200,10)])
print solve(2, 2, [(100,20), (200,10)])
print solve(3, 2, [(100,10), (100,10), (100, 10)])
print solve(4, 2, [(9,3), (7,1), (10, 1), (8,4)])

with open('A.in') as f:
	t = int(f.readline())
	for case in xrange(t):
		n, k = map(int, f.readline().split())
		pancakes = []
		for i in xrange(n):
			r, h = map(int, f.readline().split())
			pancakes.append((r, h))
		with open('A.out', 'a') as f2:
			f2.write('Case #%d: %.10f\n' % (case + 1, solve(n,k,pancakes)))
			
	