import sys

sys.setrecursionlimit(10 ** 7)

def doit(W, H, b):
	global R, N, placed
	if W <= 0 or H <= 0: return
	if placed == N: return
	r = R[placed][0]
	w = h = 2 * r
	if b & 1: w -= r
	if b & 2: h -= r
	x, y = w - r, h - r
	if x > W or y > H: return
	if (w > W and not (b & 4)) or (h > H and not (b & 8)): return

	yield (x, y)
	placed += 1
	for (x, y) in doit(W - w, h, (b & 6) | ((b & 8) if h == H else 0)): yield (x + w, y)
	for (x, y) in doit(w, H - h, (b & 9) | ((b & 4) if w == W else 0)): yield (x, y + h)
	for (x, y) in doit(W - w, H - h, b & 12): yield (x + w, y + h)

def solve():
	global N, R, placed
	N, W, H = map(int, raw_input().split())
	x = map(int, raw_input().split())
	R = sorted([(r, i) for i, r in enumerate(x)], reverse = True)
	placed = 0
	points = list(doit(W, H, 15))
	res = [None] * (2 * N)
	for i in xrange(N):
		p = R[i][1]
		res[2 * p] = points[i][0]
		res[2 * p + 1] = points[i][1]
		(x1, y1) = points[i]
		if x1 < 0 or x1 > W or y1 < 0 or y1 > H:
			raise ValueError
		r1 = R[i][0]
		for j in xrange(i):
			(x2, y2) = points[j]
			r2 = R[j][0]
			if (x2 - x1) ** 2 + (y2 - y1) ** 2 < (r1 + r2) ** 2:
				raise ValueError
			
	return ' '.join(map(str, res))
	

for i in xrange(input()):
	print >> sys.stderr, i + 1
	print "Case #%d: %s" % (i + 1, solve())
