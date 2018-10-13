#/usr/bin/env python

import re

#fin = file('b-sample.in')
#readline = fin.readline
readline = raw_input

T = int(readline())

def flow_to(grid, R, C):
    delta = ((0,-1),(-1,0),(1,0),(0,1))
    best_val = grid[R][C]
    best_pos = (R, C)
    for dc, dr in delta:
        c = C + dc
        r = R + dr
        if ((r < 0 or r >= len(grid)) or
            (c < 0 or c >= len(grid[0]))):
            continue
        if grid[r][c] < best_val:
            best_val = grid[r][c]
            best_pos = (r,c)
    return best_pos

def do_flow(grid, ans, r, c, v):
    if ans[r][c] is not None:
        return ans[r][c]
    
    R, C = flow_to(grid, r, c)
    if R == r and C == c:
        ans[r][c] = v
    else:
        ans[r][c] = do_flow(grid, ans, R, C, v)
    return ans[r][c]

for t in range(T):
    H, W = map(int, readline().split())
    grid = []
    ans = []
    for r in range(H):
        ans.append([None]*W)
        grid.append(map(int, readline().split()))
    print "Case #%d:" % (t+1)
    v = 0
    for r in range(H):
        for c in range(W):
            v = max(do_flow(grid, ans, r, c, v) + 1, v)
        print ' '.join(chr(i + ord('a')) for i in ans[r])
    
