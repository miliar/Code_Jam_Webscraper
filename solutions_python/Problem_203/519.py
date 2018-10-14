t = int(input())
for i in range(1, t+1):
    r, c = map(int, input().split())
    grid = []
    for j in range(r):
        grid.append(list(input()))
    for j in range(r):
        temp = '?'
        for k in range(c):
            if grid[j][k] != '?':
                temp = grid[j][k]
            else:
                grid[j][k] = temp
    for j in range(r):
        temp = '?'
        for k in range(c-1, -1, -1):
            if grid[j][k] != '?':
                temp = grid[j][k]
            else:
                grid[j][k] = temp
    for j in range(c):
        temp = '?'
        for k in range(r-1, -1, -1):
            if grid[k][j] != '?':
                temp = grid[k][j]
            else:
                grid[k][j] = temp
    for j in range(c):
        temp = '?'
        for k in range(r):
            if grid[k][j] != '?':
                temp = grid[k][j]
            else:
                grid[k][j] = temp
    print("Case #{}:".format(i))
    for j in range(r):
        print(''.join(grid[j]))