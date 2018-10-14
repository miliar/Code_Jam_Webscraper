import sys

from unionfind import UnionFind, Node

def neighbours(grid, x, y):
  n = []
  if 0 <= y < len(grid):
    if x - 1 >= 0:
      n.append( (grid[y][x-1], 'BW', (x-1,y)) ) #West
    if x + 1 < len(grid[0]):
      n.append( (grid[y][x+1], 'CE', (x+1,y)) ) #East
  if 0 <= x <= len(grid[0]):
    if y - 1 >= 0:  
      n.append( (grid[y-1][x], 'AN', (x,y-1)) ) #North
    if y + 1 < len(grid):
      n.append( (grid[y+1][x], 'DS', (x,y+1)) ) #South
  return n

if __name__ == "__main__":
  f = open(sys.argv[1])
  totalcases = int(f.readline())
  for casenum in xrange(totalcases):
    y, x = [int(i) for i in f.readline().split()]
    
###    print [(i,j) for i in xrange(x) for j in xrange(y)]
    uf = UnionFind( [(i,j) for i in xrange(x) for j in xrange(y)] )
    
    grid = []
    for j in xrange(y):
      grid.append( [int(i) for i in f.readline().split()] )

###    print neighbours(grid, 1, 1)

    for j in xrange(y):
    	for i in xrange(x):
    		height = grid[j][i]
    		n = sorted(neighbours(grid, i, j))
    		# Check if I'm a sink
    		if not n or not min(k[0] for k in n) < height:
    			pass
    		else:
    			# Else flow to the lowest neighbour
    			_, __, coord = n[0]
    			uf.union((i,j), coord)

###    for line in grid:
###    	print line

    letters = list("abcdefghijklmnopqrstuvwxyz")
    print "Case #%d:" % (casenum+1)
    key = {}
    for j in xrange(y):
    	for i in xrange(x):
    		node = uf.find( (i,j) ).id
    		if node not in key:
    			key[node] = letters.pop(0)
    		print key[node],
    	print
