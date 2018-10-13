import sys

size = 102

def create_grid():
    grid = []
    for i in range(size):
        grid.append([0]*size)
    return grid

def bacteria(R, rects):

    #print R, rects
    
    count = 0
    #size = 10
    
    grid = create_grid()

    for rect in rects:
        x1, y1, x2, y2 = rect
        for j in range(x1, x2+1):
            for i in range(y1, y2+1):
                grid[i][j] = 1
    
    while not is_grid_empty(grid):
        grid = iter_grid(grid)
        count += 1
    

    #print '\ngrid'
    #for row in grid:
    #    print row
    #print ''
    #print grid

    return count

def is_grid_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                return False
    return True

def iter_grid(grid):
    new_grid = create_grid()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1 and (grid[y-1][x] == 1 or grid[y][x-1] == 1):
                new_grid[y][x] = 1
            elif grid[y][x] == 0 and (grid[y-1][x] == 1 and grid[y][x-1] == 1):
                new_grid[y][x] = 1
    return new_grid

if __name__ == '__main__':
    ntests = int(sys.stdin.readline())
    for i in range(1, ntests+1):
        R = int(sys.stdin.readline())
        rects = []
        for j in range(R):
            rects.append(map(int, sys.stdin.readline().strip().split()))
        ans = bacteria(R, rects)
        print 'Case #%s: %s' %  (i, ans)
