def ok(a, r, c, d):
	dirs = {
		'^': [-1, 0],
		'<': [0, -1],
		'v': [1, 0],
		'>': [0, 1],
	}
	n = len(a)
	m = len(a[0])
	dr, dc = dirs[d]
	while True:
		r += dr
		c += dc
		if r >= n or r < 0 or c >= m or c < 0: return False
		if (a[r][c] != '.'): return True

def solve():
	r, c = map(int, raw_input().split())
	a = [raw_input() for _ in xrange(r)]
	res = 0
	for i in xrange(r):
		for j in xrange(c):
			if a[i][j] == '.': continue
			if ok(a, i, j, a[i][j]): continue
			if (not ok(a, i, j, '^')) and (not ok(a, i, j, '<')) and (not ok(a, i, j, '>')) and(not ok(a, i, j, 'v')):
				return "IMPOSSIBLE"
			res += 1
	return res
	

for i in xrange(input()):
	print "Case #%d: %s" % (i + 1, solve())
