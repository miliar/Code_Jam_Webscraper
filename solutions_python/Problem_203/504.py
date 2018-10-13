import sys

T = int(sys.stdin.readline().strip())

for t in range(T):
    R, C = [int(i) for i in sys.stdin.readline().split()]

    grid = []
    for r in range(R):
        line = list(sys.stdin.readline().strip())

        for c in range(1, C):
            if line[c] == "?" and line[c-1] != "?":
                line[c] = line[c-1]

        for c in range(C-2, -1, -1):
            if line[c] == "?" and line[c+1] != "?":
                line[c] = line[c+1]

        grid.append(line)

    for r in range(1, R):
        if grid[r][0] == "?" and grid[r-1][0] != "?":
            grid[r] = grid[r-1]

    for r in range(R-2, -1, -1):
        if grid[r][0] == "?" and grid[r+1][0] != "?":
            grid[r] = grid[r+1]

    print("Case #{}:".format(t+1))
    for r in range(R):
        print("".join(grid[r]))

