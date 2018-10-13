import math

T = int(input())
for k in range(T):
	N, K = [int(x) for x in input().split()]
	pancakes = []
	for i in range(N):
		r, h = [float(x) for x in input().split()]
		pancakes.append((r, h))
	pancakes.sort(reverse = True)
	best = 0.0
	for i, p in enumerate(pancakes):
		top = math.pi*p[0]*p[0]
		rest = [h*r for (r, h) in pancakes[i+1:]]
		if len(rest) < K-1:
			continue
		rest.sort(reverse=True)
		area = top + 2*math.pi*(p[0]*p[1] + sum(rest[:K-1]))
		best = max(best, area)
	print("Case #%d: %f" % (k+1, best))