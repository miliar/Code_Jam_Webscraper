T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    grid = []
    for r in range(R):
        grid += [list(input().strip())]


    for r in range(R):
        last_char = '?'
        for c in range(C):
            if grid[r][c] != '?':
                last_char = grid[r][c]
            elif last_char != '?':
                grid[r][c] = last_char
        last_char = '?'
        for c in range(C-1,-1,-1):
            if grid[r][c] != '?':
                last_char = grid[r][c]
            elif last_char != '?':
                grid[r][c] = last_char
    for c in range(C):
        last_char = '?'
        for r in range(R):
            if grid[r][c] != '?':
                last_char = grid[r][c]
            elif last_char != '?':
                grid[r][c] = last_char
        last_char = '?'
        for r in range(R-1,-1,-1):
            if grid[r][c] != '?':
                last_char = grid[r][c]
            elif last_char != '?':
                grid[r][c] = last_char

    print("Case #%d:" % (t+1))
    for r in range(R):
        print(''.join(grid[r]))
