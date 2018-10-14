def solve(r,c,grid):
    s = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] != '?':
                fill_h(grid,r,c,i,j)

    for i in range(r):
        for j in range(c):
            if grid[i][j] != '?':
                fill_v(grid,r,c,i,j)

    return '\n'.join(map(''.join,grid))

def fill_h(grid,r,c,y,x):
    for j in range(x-1,-1,-1):
        if grid[y][j]=='?':
            grid[y][j] = grid[y][x]
        else:
            break

    for j in range(x+1,c):
        if grid[y][j] == '?':
            grid[y][j] = grid[y][x]
        else:
            break

def fill_v(grid,r,c,y,x):
    for i in range(y-1,-1,-1):
        if grid[i][x]=='?':
            grid[i][x] = grid[y][x]
        else:
            break

    for i in range(y+1,r):
        if grid[i][x] =='?':
            grid[i][x] = grid[y][x]
        else:
            break

_T = int(input())
for _i in range(1, _T + 1):
    r,c = map(int, input().split(" "))
    grid = []
    for i in range(r):
        grid.append(list(input()))
    print("Case #%d: \n%s" % (_i, solve(r,c,grid)))

