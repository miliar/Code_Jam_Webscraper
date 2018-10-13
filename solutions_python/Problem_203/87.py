def update(grid, x, y, R, C):
    ch = grid[y][x]
    left = x
    right = x
    for i in range(x-1,-1,-1):
        if grid[y][i] == '?':
            grid[y][i] = ch 
            left = i
        else:
            break
            
    for i in range(x+1,C):
        if grid[y][i] == '?':
            grid[y][i] = ch 
            right = i
        else:
            break

    for i in range(y-1,-1,-1):
        if all(c == '?' for c in grid[i][left:(right+1)]):
            for z in range(left, right+1):
                grid[i][z] = ch
        else:
            break
            
    for i in range(y+1,R):
        if all(c == '?' for c in grid[i][left:(right+1)]):
            for z in range(left, right+1):
                grid[i][z] = ch
        else:
            break
    

def printgrid(grid):
    for row in grid:
        print(''.join(row))

def main_code(t):
    R, C = tuple(map(int, input().split()))
    grid = [list(input()) for _ in range(R)]
    done = {'?'}
    for y in range(R):
        for x in range(C):
            ch = grid[y][x]
            if ch in done:
                continue
            update(grid, x, y, R, C)
            done.add(ch)

    print("Case #" + str(t) + ":")
    printgrid(grid)

T = int(input())
for x in range(T):
    main_code(x + 1)
