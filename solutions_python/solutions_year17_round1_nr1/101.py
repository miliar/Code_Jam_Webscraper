T = int(input())

for t in range(1, T+1):
    R, C = [int(x) for x in input().split()]
    grid = []
    for r in range(R):
        grid.append(list(input()))
        cnt = 0
        for c in range(C):
            if grid[r][c] != '?':
                cnt += 1
        if cnt == 1:
            for c in range(C):
                if grid[r][c] != '?':
                    gold = grid[r][c]
            for c in range(C):
                grid[r][c] = gold
        elif cnt > 1:
            prev = 0
            c = 0
            while c < C:
                if grid[r][c] != '?':
                    for i in range(prev, c):
                        grid[r][i] = grid[r][c]
                    prev = c + 1
                    c = prev
                else:
                    c += 1
            if prev != C:
                for i in range(prev, C):
                    grid[r][i] = grid[r][prev - 1]
    r = 0
    prev = 0
    while r < R:
        if grid[r][0] != '?':
            for i in range(prev, r):
                for j in range(C):
                    grid[i][j] = grid[r][j]
            prev = r + 1
            r = prev
        else:
            r += 1
    if prev != R:
        for i in range(prev, R):
            for j in range(C):
                grid[i][j] = grid[prev - 1][j]
    print(f'Case #{t}:')
    for r in range(R):
        print(''.join(grid[r]))

