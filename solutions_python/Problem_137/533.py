import numpy as np

def show_grid():
    for i in range(R):
        line = ""
        for j in range(C):
            line += grid[i][j]
        print line

def can_be_zero(x, y, remain):
    dxs = [-1, -1, -1, 0, 1, 1,  1,  0]
    dys = [-1,  0,  1, 1, 1, 0, -1, -1]

    count = 0
    for dx, dy in zip(dxs, dys):
        if 0 <= x+dx < R and 0 <= y+dy < C:
            if grid[x+dx, y+dy] == '*':
                count += 1

    return remain >= count

def dfs(x, y, remain):
    # print "="*10
    # print x, y, remain
    # print grid

    if remain == 0:
        # print grid
        return 1

    if not can_be_zero(x, y, remain):
        return 0

    dxs = [-1, -1, -1, 0, 1, 1,  1,  0, 0]
    dys = [-1,  0,  1, 1, 1, 0, -1, -1, 0]

    count = 0
    changed_dxs = []
    changed_dys = []

    for dx, dy in zip(dxs, dys):
        if 0 <= x+dx < R and 0 <= y+dy < C:
            if grid[x+dx, y+dy] == '*':
                grid[x+dx, y+dy] = '.'
                count += 1
                changed_dxs.append(dx)
                changed_dys.append(dy)

    if count == 0:
        return 0

    ## dxs2 = [-2, -2, -2, -2, -2, -1, 0, 1, 2, 2, 2,  2,  2,  1,  0, -1]
    ## dys2 = [-2, -1,  0,  1,  2,  2, 2, 2, 2, 1, 0, -1, -2, -2, -2, -1]

    for dx, dy in zip(dxs, dys):
        if 0 <= x+dx < R and 0 <= y+dy < C:
            if dfs(x+dx, y+dy, remain-count):
                return 1

    for dx, dy in zip(changed_dxs, changed_dys):
        grid[x+dx, y+dy] = '*'

    return 0

def solve(n):
    print "Case #{:d}:".format(n+1)
    flag = False
    for i in range(R):
        for j in range(C):
            grid[0, 0] = 'c'
            remain = R*C-M-1
            if dfs(0, 0, remain):
                flag = True
                show_grid()
                break
        if flag:
            break
    if not flag:
        print "Impossible"


if __name__ == '__main__':
    T = int(raw_input())
    for n in range(T):
        R, C, M = [int(x) for x in raw_input().split()]
        grid = np.array([list("*"*C) for i in range(R)])
        solve(n)
