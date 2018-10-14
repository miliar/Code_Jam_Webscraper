import fileinput
stdin = fileinput.input()

def solveCase():
	R,C = map(int,stdin.next().split())
	rows = [stdin.next()[:-1] for r in xrange(R)]
	t = {(x,y):rows[y][x] for x in xrange(C) for y in xrange(R)}
	horFill = [sum(1 for x in xrange(C) if t[(x,y)]!='.') for y in xrange(R)]
	verFill = [sum(1 for y in xrange(R) if t[(x,y)]!='.') for x in xrange(C)]
	dirs = {'>':(1,0),'<':(-1,0),'^':(0,-1),'v':(0,1)}
	e = set()
	for x in xrange(C):
		for y in xrange(R):
			if t[(x,y)]!='.':
				if verFill[x]==1 and horFill[y]==1:
					return "IMPOSSIBLE"
				dx,dy = dirs[t[(x,y)]]
				x2,y2 = x,y
				while True:
					x2,y2 = x2+dx,y2+dy
					if x2<0 or y2<0 or y2>=R or x2>=C:
						e.add((x2,y2))
						break
					if t[(x2,y2)]!='.':
						break
	return len(e)

for case in xrange(int(stdin.next())):
	print "Case #{0}: {1}".format(case+1,solveCase())