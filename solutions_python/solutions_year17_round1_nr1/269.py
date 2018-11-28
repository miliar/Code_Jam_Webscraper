T = int(input())

for t in range(T):
    R, C = map(int, input().split())

    grid = []
    for _ in range(R):
        grid.append(list(input()))

    for i in range(R):
        last = "?"
        first = None
        for j in range(C):
            if grid[i][j] != "?":
                last = grid[i][j]
                if not first:
                    first = last
            else:
                grid[i][j] = last
        if first:
            for j in range(C):
                if grid[i][j] == "?":
                    grid[i][j] = first
        elif i > 0:
            for j in range(C):
                grid[i][j] = grid[i-1][j]

    for i in reversed(range(R)):
        for j in range(C):
            if grid[i][j] == "?":
                grid[i][j] = grid[i+1][j]

    print("Case #{}:".format(t+1))
    print("\n".join("".join(l) for l in grid))
