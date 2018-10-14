
directions = {
    '^':(-1,0),
    'v':(1,0),
    '<':(0,-1),
    '>':(0,1),
    '.':(0,0)
}

def stays(grid,i0,j0,(d_i,d_j)):
    if (d_i,d_j) == (0,0):
        return True
    i,j=i0,j0
    while 1:
        i += d_i
        j += d_j
        if not (0<=i<len(grid) and 0<=j<len(grid[0])):
            break
        if grid[i][j] != '.':
            return True
    return False

def solve(grid):
    n = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if stays(grid,i,j,directions[grid[i][j]]):
                continue
            possible = False
            for arrow in '^v><':
                if arrow == grid[i][j]:
                    continue
                if stays(grid,i,j,directions[arrow]):
                    n += 1
                    possible = True
                    break
            if not possible:
                return "IMPOSSIBLE"
    return str(n)

n_cases = input()
for case in range(1,n_cases + 1):
    r,c = map(int,raw_input().split(' '))
    grid = [raw_input() for _ in range(r)]
    solution = solve(grid)
    print "Case #%d: %s" % (case,solution)