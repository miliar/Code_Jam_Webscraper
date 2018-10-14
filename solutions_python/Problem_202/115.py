from collections import namedtuple

Grid = namedtuple("Grid", ["N", "pluses", "crosses"])

def check_rows_cols(crosses):
    N = len(crosses)
    assert( all( sum(row)==1 for row in crosses ) )
    for c in range(N):
        assert( sum(crosses[r][c] for r in range(N))==1 )

def do_rows_cols(crosses):
    N = len(crosses)
    rows, cols = set(), set()
    for i in range(N):
        for j in range(N):
            if crosses[i][j] == 1:
                rows.add(i)
                cols.add(j)
    allowed_rows = set(range(N)).difference(rows)
    allowed_cols = set(range(N)).difference(cols)
    for r, c in zip(allowed_rows, allowed_cols):
        crosses[r][c] = 1
    check_rows_cols(crosses)

def check_diags(pluses):
    N = len(pluses)
    data = dict()
    for i in range(N):
        for j in range(N):
            co = (i+j, i-j)
            if co not in data:
                data[co] = 0
            data[co] += 1
    assert(all(x<=1 for x in data.values()))

def add_top_row(pluses, c):
    N = len(pluses)
    okay = True
    i = 0
    while c-i >= 0:
        if pluses[i][c-i] == 1:
            okay = False
        i += 1
    i = 0
    while c+i < N:
        if pluses[i][c+i] == 1:
            okay = False
        i += 1
    if okay:
        pluses[0][c] = 1

def add_bottom_row(pluses, c):
    N = len(pluses)
    okay = True
    i = 0
    while c-i >= 0:
        if pluses[N-1-i][c-i] == 1:
            okay = False
        i += 1
    i = 0
    while c+i < N:
        if pluses[N-1-i][c+i] == 1:
            okay = False
        i += 1
    if okay:
        pluses[N-1][c] = 1

def do_diags(pluses):
    N = len(pluses)
    # Add to top / botom row if possible
    for i in range(N):
        add_top_row(pluses, i)
        add_bottom_row(pluses, i)
    check_diags(pluses)

def make(crosses, pluses):
    N = len(crosses)
    g = [["." for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if crosses[i][j] == 1:
                g[i][j] = "x"
            if pluses[i][j] == 1:
                g[i][j] = "+"
            if crosses[i][j] == 1 and pluses[i][j] == 1:
                g[i][j] = "o"
    return g

def copy(g):
    return list( list(row) for row in g )

def answer(grid):
    old = make(grid.crosses, grid.pluses)
    do_rows_cols(grid.crosses)
    do_diags(grid.pluses)
    count = sum(sum(row) for row in grid.crosses)
    count += sum(sum(row) for row in grid.pluses)
    new = make(grid.crosses, grid.pluses)
    diffs = []
    for i in range(grid.N):
        for j in range(grid.N):
            if old[i][j] != new[i][j]:
                diffs.append("{} {} {}".format(new[i][j],i+1,j+1))
    out = "{} {}".format(count, len(diffs))
    diffs.insert(0, out)
    return "\n".join(diffs)

grid = Grid(1, [[1]], [[1]])
assert(answer(grid) == "2 0")
grid = Grid(2, [[0,0],[0,0]], [[0,0],[0,0]])
assert(answer(grid) == "4 3\no 1 1\n+ 2 1\nx 2 2")
grid = Grid(3, [[0,0,0],[1,1,1],[0,0,0]], [[0,0,0],[0,0,0],[1,0,0]])
assert(answer(grid) == "6 2\nx 1 2\no 2 3")

import sys
with open(sys.argv[1]) as input:
    number = int(next(input))
    data = []
    for _ in range(number):
        N, M = [int(x) for x in next(input).strip().split()]
        pluses = [[0 for _ in range(N)] for _ in range(N)]
        crosses = [[0 for _ in range(N)] for _ in range(N)]
        for _ in range(M):
            line = next(input).strip().split()
            row, col = int(line[1]), int(line[2])
            if line[0] == "o" or line[0] == "+":
                pluses[row-1][col-1] = 1
            if line[0] == "o" or line[0] == "x":
                crosses[row-1][col-1] = 1
        data.append(Grid(N, pluses, crosses))

with open(sys.argv[2], "w") as output:
    for i, g in enumerate(data):
        print("Case #{}: {}".format(i+1, answer(g)), file=output)
