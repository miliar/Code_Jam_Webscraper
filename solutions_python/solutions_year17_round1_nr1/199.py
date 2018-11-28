from functools import reduce

def solve(grid, i, r, c):
    if i == r:
        return

    initials = [c for c in grid[i] if c != '?']
    if initials:
        x = initials[0]
        for j in range(c):
            if grid[i][j] == '?':
                grid[i][j] = x
            else:
                x = grid[i][j]
        solve(grid, i+1, r, c)
    else:
        if i-1 >= 0 and all(c != '?' for c in grid[i-1]):
            for j in range(c):
                grid[i][j] = grid[i-1][j]
            solve(grid, i+1, r, c)
        elif i+1 < r:
            solve(grid, i+1, r, c)
            for j in range(c):
                grid[i][j] = grid[i+1][j]
        else:
            raise Exception('Should not be reached here')

for case in range(1, int(input())+1):
    R, C = input().split()
    grid = []
    for r in range(int(R)):
        grid.append(list(input()))
    solve(grid, 0, int(R), int(C))
    print('Case #{}:'.format(case))
    for r in range(int(R)):
        print(''.join(grid[r]))
