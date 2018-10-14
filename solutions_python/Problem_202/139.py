import copy
import random
def shufflerange(n):
	r = range(n)
#	if n > 1: rng.insert(1, rng.pop())
	random.shuffle(r)
#	q = r[2:]
#	r = r[:2]
#	random.shuffle(q)
#	r += q
#	print r
	return r


def check(y, x):
	c = a[y][x]
	assert c != "."

	if c != "+":
		if sum(c in "ox" for c in a[y]) > 1: return False
		if sum(a[y2][x] in "ox" for y2 in xrange(N)) > 1: return False

	if c != "x":
		i1 = -min(x, y)
		i2 = min(N - x, N - y)
		if sum(a[y + i][x + i] in "o+" for i in xrange(i1, i2)) > 1: return False
		i1 = -min(N - x - 1, y)
		i2 = min(x + 1, N - y)
		if sum(a[y + i][x - i] in "o+" for i in xrange(i1, i2)) > 1: return False

	return True


for _ in xrange(input()):
	N, M = map(int, raw_input().split())
	a = [["."] * N for r in xrange(N)]
	for i in xrange(M):
		t, y, x = raw_input().split()
		a[int(y) - 1][int(x) - 1] = t
	b = copy.deepcopy(a)

	# x and +
	rng = range(N)
	if N > 1: rng.insert(1, rng.pop())

	for y in rng:
		for x in range(N):
			if a[y][x] != ".": continue
			a[y][x] = "+"
			if check(y, x): continue
			a[y][x] = "."

	for y in rng:
		for x in range(N):
			if a[y][x] != ".": continue
			a[y][x] = "x"
			if check(y, x): continue
			a[y][x] = "."

	# o
	for y in range(N):
		for x in range(N):
			c = a[y][x]
			if c not in "+x": continue
			a[y][x] = "o"
			if check(y, x): continue
			a[y][x] = c


	# cout score
	score = sum("..x+o".find(c) / 2 for r in a for c in r)
	dif = []
	for y in xrange(N):
		for x in xrange(N):
			if a[y][x] != b[y][x]:
				dif.append("%c %d %d" % (a[y][x], y+1, x+1))

#	for r in b: print "".join(r)
#	print
#	for r in a: print "".join(r)


	print "Case #%d:" % (_ + 1), score, len(dif)
	for l in dif: print l

