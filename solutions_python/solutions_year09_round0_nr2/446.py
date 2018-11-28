import sys

counts = sys.stdin.readline().split()
N = int(counts[0])
W = 0
H = 0
alts = list()
edges = list()
chars = {}
dirs = {}

def calc_edge(x, y):
	global alts, dirs, edges, W, H
	c = (x, y)
	d = c
	m = alts[y][x]
	if y < H - 1:
		if alts[y + 1][x] <= m:
			m = alts[y + 1][x]
			d = (x, y + 1)
	if x < W - 1:
		if alts[y][x + 1] <= m:
			m = alts[y][x + 1]
			d = (x + 1, y)
	if x > 0:
		if alts[y][x - 1] <= m:
			m = alts[y][x - 1]
			d = (x - 1, y)
	if y > 0:
		if alts[y - 1][x] <= m:
			m = alts[y - 1][x]
			d = (x, y - 1)
	if m == alts[y][x]: d = c
	dirs[c] = d
	if c != d: edges.append((c, d))

def flood_recur(c, letter):
	global edges, chars
	chars[c] = letter
	for (d, e) in filter(lambda (a,b): b == c, edges):
		if chars[d] == '#': flood_recur(d, letter)

def flood(x, y):
	global dirs, letter
	c = (x, y)
	if dirs[c] == c:
		flood_recur(c, chr(letter))
		letter += 1

def rename_cell(x, y):
	global newname, letter, chars
	if chars[(x, y)] not in newnames:
		newnames[chars[(x, y)]] = chr(letter)
		letter += 1
	chars[(x, y)] = newnames[chars[(x, y)]]

for k in xrange(N):
	counts = sys.stdin.readline().split()
	H = int(counts[0])
	W = int(counts[1])
	alts = list()
	edges = list()
	chars = {}
	dirs = {}
	for h in xrange(H):
		alts.append(sys.stdin.readline().split())
	for w in xrange(W):
		for h in xrange(H):
			calc_edge(w, h)
			chars[(w, h)] = '#'
	letter = ord('a')
	for h in xrange(H):
		for w in xrange(W):
			flood(w, h)
	letter = ord('a')
	newnames = {}
	for h in xrange(H):
		for w in xrange(W):
			rename_cell(w, h)
	print 'Case #%d:' % (k + 1)
	for h in xrange(H):
		for w in xrange(W):
			print chars[(w, h)],
		print ''

