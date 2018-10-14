import sys
sys.stdout = open('a_big.out', 'w')
sys.stdin  = open("a_big.in", 'r')
sys.setrecursionlimit(1500)


def empty(row):
    for c in row:
        if c != '?':
            return False
    return True

def filled_out(row):
    for c in row:
        if c == '?':
            return False
    return True

def should_fill(row):
    a, b = 0, 0
    for c in row:
        if c == '?':
            a += 1
        else:
            b += 1
    return (a != 0 and b != 0)

def fill_out(row):
    first = 0
    for i in range(len(row)):
        #print i
        if row[i] != '?':
            for j in range(first, i):
                row[j] = row[i]
            first = i
            while i + 1 < len(row) and row[i + 1] == '?':
                row[i + 1] = row[first]
                i = i + 1
            first = i + 1
    return row

def algorithm(grid):
    #print grid
    can_fill = True
    while can_fill:
        can_fill = False
        for row in grid:
            if should_fill(row):
                can_fill = True
                fill_out(row)
    some_empty = True
    while some_empty:
        some_empty = False
        for i, row in enumerate(grid):
            if empty(row):
                some_empty = True
                if i > 0:
                    if not empty(grid[i - 1]):
                        grid[i] = grid[i - 1]
                    elif i < len(grid) - 1:
                        grid[i] = grid[i + 1]
                else:
                    grid[i] = grid[i + 1]
    return





def solve():
    R, C = map(int, raw_input().split())
    grid = []
    for _ in range(R):
        grid.append(list(raw_input().strip()))
        assert len(grid[-1]) == C
    algorithm(grid)

    return '\n' + '\n'.join(map(lambda r: "".join(r), grid))


T = int(raw_input())
for i in range(1, T + 1):
    ans = solve()
    print "Case #" + str(i) + ": " + str(ans)