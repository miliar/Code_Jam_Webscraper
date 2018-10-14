import fileinput

def extend(a, r, c, sx, sy):
	l = []
	for dy in range(-1, 2):
		for dx in range(-1, 2):
			if dy == 0 and dx == 0: continue
			x, y = sx+dx, sy+dy
			if x >= 0 and x < c and y >= 0 and y < r and a[y][x] == '*': l.append((x, y))
	return l

def rec(a, r, c, w, sx, sy, z):
	l = extend(a, r, c, sx, sy)
	if not l: return False

	for x, y in l: a[y][x] = '.'
	z += len(l)

	if z == w: return True
	if z > w:
		for x, y in l: a[y][x] = '*'
		z -= len(l)
		return False

	for dy in range(-1, 2):
		for dx in range(-1, 2):
			if dy == 0 and dx == 0: continue
			x, y = sx+dx, sy+dy
			if x >= 0 and x < c and y >= 0 and y < r and a[y][x] == '.':
				a[y][x] = 'x'
				if rec(a, r, c, w, x, y, z): return True
				a[y][x] = '.'

	for x, y in l: a[y][x] = '*'
	z -= len(l)

	return False

def solve(r, c, m):
	n = r*c
	w = n-m
	a = [['*' for i in range(c)] for j in range(r)]
	a[0][0] = 'x'
	if w == 1 or rec(a, r, c, w, 0, 0, 1):
		a[0][0] = 'c'
		for l in a: print("".join(l).replace("x", "."))
	else:
		print("Impossible")

f = fileinput.input()
for t in range(1, 1+int(f.readline())):
	r, c, m = list(map(int, f.readline().rstrip().split()))
	print("Case #%d:" % t)
	solve(r, c, m)