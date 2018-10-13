from collections import defaultdict

def solve(grid, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "." and grid[r].count(".") == cols-1 and [grid[i][c] for i in range(rows)].count(".") == rows-1:
                return "IMPOSSIBLE"

    edges = set()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == ">":
                C = c + 1
                while C < cols:
                    if grid[r][C] != ".":
                        edges.add(((r,c), (r,C)))

                    C += 1

            elif grid[r][c] == "<":
                C = c - 1
                while C >= 0:
                    if grid[r][C] != ".":
                        edges.add(((r,c), (r,C)))

                    C -= 1

            elif grid[r][c] == "^":
                R = r - 1
                while R >= 0:
                    if grid[R][c] != ".":
                        edges.add(((r,c), (R,c)))

                    R -= 1

            elif grid[r][c] == "v":
                R = r + 1
                while R < rows:
                    if grid[R][c] != ".":
                        edges.add(((r,c), (R,c)))

                    R += 1

    s = {p[0] for p in edges}
    t = {(r,c) for r in range(rows) for c in range(cols) if grid[r][c] != "."}

    return len(t-s)

with open("A.out", "w") as outfile:
    with open("A-large.in") as infile:
        ncases = int(next(infile))

        for case in range(1, ncases + 1):
            rows, cols = map(int, next(infile).split())
            grid = []

            for r in range(rows):
                grid.append(list(next(infile).rstrip()))

            print("Case #%d: %s" % (case, solve(grid, rows, cols)), file=outfile)
