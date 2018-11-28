import sys
from collections import defaultdict

iname = sys.argv[1]
oname = iname.rstrip('in') + "out"
result = ""
with open(iname, "rb") as f:
    cases = int(f.readline().strip())
    for case in range(cases):
        line = f.readline().strip()
        result += "Case #%d:\n" % (case + 1)
        R, C = map(int, line.split())
        grid = [[0 for i in range(C)] for j in range(R)]
        for r in range(R):
            line = list(f.readline().strip())
            last = ""
            lastpos = -1
            for c in range(C):
                if line[c] != "?":
                    grid[r][c] = line[c]
                    last = line[c]
                    for i in range(lastpos + 1, c):
                        grid[r][i] = last
                    lastpos = c
                else:
                    if c == C - 1 and last:
                        for i in range(lastpos, c + 1):
                            grid[r][i] = last
        nonempty = 0
        for r in range(R):
            if all(grid[r]):
                nonempty = r
                for i in range(r):
                    for c in range(C):
                        grid[i][c] = grid[r][c]
                break
        for r in range(nonempty, R):
            if not all(grid[r]):
                for c in range(C):
                    grid[r][c] = grid[r - 1][c]

        for r in range(R):
            line = "".join(grid[r]) + "\n"
            result += line 

with open(oname, "wb") as f:
    f.write(result)
