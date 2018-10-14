import sys

def solve(grid, casen):
    r = len(grid)
    c = len(grid[0])
    for i in xrange(r-1):
        for j in xrange(c-1):
            if not grid[i][j] == '#':
                continue
            if grid[i][j+1] == '#' and grid[i+1][j] == '#' and grid[i+1][j+1] == '#':
                grid[i][j] = '/'
                grid[i][j+1] = '\\'
                grid[i+1][j] = '\\'
                grid[i+1][j+1] = '/'
    print "Case #%d:" % casen
    for row in grid:
        if row.count('#'):
            print "Impossible"
            return
    for row in grid:
        print ''.join(row)
            

if __name__ == '__main__':
    with open(sys.argv[1], 'rU') as f:
        lines = f.readlines()
        ncases = int(lines[0])
        lines = lines[1:]
        for i in xrange(ncases):
            grid = []
            r, c = map(int, lines[0].strip().split(' '))
            lines = lines[1:]
            for j in xrange(r):
                grid.append(list(lines[0].strip()))
                lines = lines[1:]
            solve(grid, i+1)
