import sys

name = "B-small-attempt0"
path = "d:/"
sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

inp = lambda: map(int, input().split())

testCases = next(inp())

for testCase in range(testCases):
    n, m = inp()

    h = []
    for r in range(n):
        h.append([x for x in inp()])

    rows = [0] * n
    cols = [0] * m

    for r in range(n):
        for c in range(m):
            rows[r] = max(rows[r], h[r][c])
            cols[c] = max(cols[c], h[r][c])

    h1 = [[0] * m for i in range(n)]

    for r in range(n):
        for c in range(m):
            h1[r][c] = min(rows[r], cols[c])

    res = "YES" if h == h1 else "NO"
    print("Case #" + str(testCase + 1) + ": " + res)
