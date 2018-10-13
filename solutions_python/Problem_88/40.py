# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
T = int(fin.readline())

def moment(grid):
    rows = []
    for row in grid:
        rr = map(lambda (i, v): (i)*v, enumerate(row))
        rrr = [0]
        last = 0
        for col in rr:
            last += col
            rrr.append(last)
        rows.append(rrr)
    
    blocks = []
    last = [0]*len(rows[0])
    blocks.append(last)
    for row in rows:
        last = map(lambda (a,b): a+b, zip(last, row))
        blocks.append(last)
    return blocks
    
def weight(grid):
    rows = []
    for row in grid:
        rrr = [0]
        last = 0
        for col in row:
            last += col
            rrr.append(last)
        rows.append(rrr)
    blocks = []
    last = [0]*len(rows[0])
    blocks.append(last)
    for row in rows:
        last = map(lambda (a,b): a+b, zip(last, row))
        blocks.append(last)
    return blocks

def total(blocks, r, c, d):
    return blocks[r][c] + blocks[r+d][c+d] - blocks[r][c+d] - blocks[r+d][c]

def tblade(blocks, r, c, d):
    return total(blocks, r, c, d) - total(blocks, r, c, 1) - total(blocks, r+d-1, c+d-1, 1) \
        - total(blocks, r+d-1, c, 1) - total(blocks, r, c+d-1, 1)

def cog(blocks, weights, r, c, d):
    m = tblade(blocks, r, c, d)
    w = tblade(weights, r, c, d)
    #print >> sys.stderr, m, w
    center = float(m)/w
    return center
    
def invert(grid):
    R = len(grid)
    C = len(grid[0])
    inverted = []
    for r in range(C):
        row = [c[r] for c in grid]
        inverted.append(row)
    return inverted

for case in range(1,T+1):
    R, C, D = map(int, fin.readline().split())
    grid = []
    for i in range(R):
        row = map(int, fin.readline().strip())
        row = map(lambda x: x + D, row)
        grid.append(row)
    
    inv = invert(grid)
    mxblocks = moment(grid)
    wxblocks = weight(grid)
    myblocks = moment(inv)
    wyblocks = weight(inv)
    
    result = "IMPOSSIBLE"
    for s in range(3, min(R, C)+1):
        for r in range(R-s+1):
            for c in range(C-s+1):
                cx = cog(mxblocks, wxblocks, r, c, s)
                cy = cog(myblocks, wyblocks, c, r, s)
                if cx == c+(s-1)/2.0 and cy == r+(s-1)/2.0:
                    result = s
                    
    #print >> sys.stderr, "Grid", grid
    #print >> sys.stderr, "Inve", invert(grid)
    #print >> sys.stderr, "Moment", mxblocks
    #print >> sys.stderr, "Weight", wxblocks
    #print >> sys.stderr, cog(mxblocks, wxblocks, 0, 0, 3)
    #print >> sys.stderr, cog(myblocks, wyblocks, 0, 0, 3)
    #print >> sys.stderr, cog(mxblocks, wxblocks, 1, 1, 5)
    #print >> sys.stderr, cog(myblocks, wyblocks, 1, 1, 5)
    
    #print >> sys.stderr
    
    print "Case #%d: %s" % (case, result)

