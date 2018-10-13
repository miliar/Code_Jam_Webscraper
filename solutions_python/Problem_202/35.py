#!/usr/bin/env python3
def upgrade(g, r, c, m):
    if g[r][c] == '.':
        g[r][c] = m
    else:
        g[r][c] = 'o'


def aug(s):
    if S[s] == False or vis[s] == time:
        return False
    vis[s] = time
    for r in range(max(s - N + 1, 0), min(s + 1, N)):
        c = s - r
        if S[s] != r:
            d = r - c
            oldr = D[d + N - 1]
            if oldr == False:
                continue

            if oldr is None or \
                    aug(oldr + (oldr - d)):
                S[s] = r
                D[d + N - 1] = r
                return True
    return False


def find_match():
    global vis, time
    vis = [0] * (2 * N - 1)
    time = 1
    f = True
    while f:
        f = False
        for s in range(2 * N - 1):
            if aug(s):
                f = True
            time += 1

    return ((r, s - r) for s, r in enumerate(S) if type(r) is int)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    R = [True] * N
    C = [True] * N
    S = [None] * (2 * N - 1)
    D = [None] * (2 * N - 1)
    grid = [['.'] * N for _ in range(N)]
    for _ in range(M):
        m, r, c = input().split()
        r, c = int(r) - 1, int(c) - 1
        grid[r][c] = m
        if m in ('x', 'o'):
            R[r] = False
            C[c] = False
        if m in ('+', 'o'):
            S[r + c] = False
            D[r - c + N - 1] = False

    newgrid = [row[:] for row in grid]
    rows = (r for r in range(N) if R[r])
    columns = (c for c in range(N) if C[c])
    for r, c in zip(rows, columns):
        upgrade(newgrid, r, c, 'x')
    for r, c in find_match():
        upgrade(newgrid, r, c, '+')

    points = {'.': 0, '+': 1, 'x': 1, 'o': 2}
    total = sum(sum(points[m] for m in row) for row in newgrid)
    diff = [(newm, r + 1, c + 1)
            for r, (row, newrow) in enumerate(zip(grid, newgrid))
            for c, (m, newm) in enumerate(zip(row, newrow))
            if m != newm]
    print("Case #{}: {} {}".format(t + 1, total, len(diff)))
    if diff:
        print("\n".join("{} {} {}".format(*t) for t in diff))
