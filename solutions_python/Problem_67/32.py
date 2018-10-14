import sys


def solve_grid(grid):
    iters = 0
    #print grid.keys()
    while grid:
        to_add = set()
        to_remove = set()
        
        for px,py in grid:
            # this cell dies if nothing above or left
            if ((px-1,py) not in grid) and ((px,py-1) not in grid):
                to_remove.add((px,py))
            # cell is born to the right if it's empty and there's a cell above and right
            if ((px+1,py) not in grid) and (px+1,py-1) in grid:
                to_add.add((px+1,py))
        
        for p in to_add:
            grid[p] = 1
        for p in to_remove:
            del grid[p]
        iters += 1
        #print iters, grid.keys()
        
    return iters

infile = sys.stdin
ntests = int(infile.readline().strip())        
for i in xrange(ntests):
    R = int(infile.readline().strip())
    grid = {}
    for j in xrange(R):
        x1,y1,x2,y2 = map(int, infile.readline().strip().split())
        for x in xrange(x1,x2+1):
            for y in xrange(y1,y2+1):
                grid[x,y] = 1
    
    result = solve_grid(grid)
    print("Case #%d: %d" % (i+1, result))