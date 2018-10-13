import sys

def works(grid):
    grid2 = zip(*grid)
    maxrows = map(max, grid)
    maxcols = map(max, grid2)
    for i in range(len(grid)):
        for j in range(len(grid2)):
            if grid[i][j] < min(maxrows[i], maxcols[j]):
                return False
    return True

def run_case():
    n, m = map(int, raw_input().split())
    grid = []
    for r in range(n):
        vals = map(int, raw_input().split())
        grid.append(vals)
    if works(grid):
        print 'YES'
    else:
        print 'NO'


ncases = int(raw_input())
for t in range(ncases):
    sys.stdout.write('Case #%s: ' % (t+1))
    run_case()
