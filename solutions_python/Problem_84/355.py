#!/usr/bin/python2
import sys

grid = []

def read_int(fp):
    return int(fp.readline())

def repl(grid):
    y = 0
    while y < (len(grid)-1):
        x = 0
        while x < (len(grid[0])-1):
            coords = [(y,x), (y,x+1), (y+1,x), (y+1,x+1)]
            #print x,y, grid[y][x]
            if all(map(lambda (x,y): grid[x][y] == '#', coords)):
                grid[y][x] = grid[y+1][x+1] = '/'
                grid[y][x+1] = grid[y+1][x] = '\\'
                #print 'repl', x, y
                x += 1

            x += 1
        y += 1

if len(sys.argv) < 2:
    print 'Usage: %s <input file>' % sys.argv[0]
    sys.exit(1)

fp = open(sys.argv[1])
cases = read_int(fp)

for t in xrange(cases):
    rows, cols = map(int, fp.readline().split())
    grid = []

    for i in xrange(rows):
        grid.append(list(fp.readline().strip()))

    #print grid
    repl(grid)

    print 'Case #%d:' % (t+1)

    if not all(map(lambda x: '#' not in x, grid)):
        print 'Impossible'
    else:
        for line in grid:
            print ''.join(line)

