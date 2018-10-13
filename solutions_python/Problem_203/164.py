def solve(grid):
    for y in range(len(grid)):
        last_index = 0
        last_char = '?'
        for x in range(len(grid[y])):
            if grid[y][x] != '?':
                grid[y][last_index:x+1] = [grid[y][x]]*len(grid[y][last_index:x+1])
                last_index = x+1
                last_char = grid[y][x]

        grid[y][last_index:x+1] = [last_char]*len(grid[y][last_index:x+1])

    for y in range(1, len(grid)):
        if '?' in grid[y]:
            grid[y] = grid[y-1]

    for y in range(len(grid)-2, -1, -1):
        if '?' in grid[y]:
            grid[y] = grid[y+1]

    return grid



with open("A-large.in") as infile:
    with open("A-large.out", "w") as outfile:
        cases = int(next(infile))

        for i in range(1, cases+1):
            h, w = map(int, next(infile).split())
            grid = []
            
            for y in range(h):
                grid.append(list(next(infile).rstrip()))

            print("Case #{}:".format(i), file=outfile)
            for row in solve(grid):
                print("".join(row), file=outfile)

