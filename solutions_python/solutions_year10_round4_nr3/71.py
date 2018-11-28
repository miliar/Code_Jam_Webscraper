from copy import copy

def evolve(cells):
	cells2 = copy(cells)
	for c in cells:
		north = (c[0], c[1]-1)
		west = (c[0]-1, c[1])
		east = (c[0]+1, c[1])
		northeast = (c[0]+1, c[1]-1)
		
		if north not in cells and west not in cells:
			cells2.remove(c)		
		if northeast in cells:
			cells2.add(east)

	return cells2
	
def solve(tc):
	k = input()
	cells = set()
	for i in xrange(k):
		x1, y1, x2, y2 = map(int, raw_input().split())
		for x in xrange(x1, x2+1):
			for y in xrange(y1, y2+1):
				cells.add((x,y))
	ans = 0
	
	while len(cells) > 0:
		cells = evolve(cells)
		ans+=1
		
	print "Case #%d:"%tc, ans

for i in xrange(input()):
	solve(i+1)