def find_parent(u, v):
	if u[v] < 0:
		return v
	u[v] = p = find_parent(u, u[v])
	return p
def merge(u, v1, v2):
	p1 = find_parent(u, v1)
	p2 = find_parent(u, v2)
	if u[p1] > u[p2]: # ||p1|| < ||p2||
		u[p1] = p2
	else:
		u[p2] = p1

def solve():
	h, w = [int(x) for x in raw_input().split()]
	v = []
	u = [-1] * (w*h)
	for y in xrange(h):
		v.append([int(x) for x in raw_input().split()])
	way = [[0,-1],[-1,0],[1,0],[0,1]]
	for y in xrange(h):
		for x in xrange(w):
			low = v[y][x]
			dir = None
			for wx, wy in way:
				nx = x + wx
				ny = y + wy
				if nx >= 0 and ny >= 0 and nx < w and ny < h:
					if low > v[ny][nx]:
						low = v[ny][nx]
						dir = nx + ny*w
			if dir is not None:
				merge(u, x+ y*w, dir)
	assign = {}
	current = 'a'
	for y in xrange(h):
		for x in xrange(w):
			p = find_parent(u, x+y*w)
			if p not in assign:
				assign[p] = current
				current = chr(ord(current)+1)
			v[y][x] = assign[p]
	for d in v:
		print ' '.join(d)
	
n = int(raw_input())
for loop in xrange(n):
	print 'Case #%d:' % (loop+1)
	solve()
