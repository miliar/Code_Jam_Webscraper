DIRECTION_X = {"UP": 0, "DOWN": 0, "LEFT": -1, "RIGHT": 1}
DIRECTION_Y = {"UP": -1, "DOWN": 1, "LEFT": 0, "RIGHT": 0}


def can_go(grid, nx, ny):
    r = len(grid)
    c = len(grid[0])
    if nx < 0 or nx >= c or ny < 0 or ny >= r:
        return False
    return True


def go_change(grid, x, y, direction):
    letter = grid[y][x]
    nx = x + DIRECTION_X[direction]
    ny = y + DIRECTION_Y[direction]
    while can_go(grid, nx, ny) and grid[ny][nx] == '?':
        grid[ny][nx] = letter
        nx += DIRECTION_X[direction]
        ny += DIRECTION_Y[direction]


def copy_column(grid, x, direction):
    nx = x + DIRECTION_X[direction]
    if can_go(grid, nx, 0):
        if grid[0][nx] == '?':
            if not copy_column(grid, nx, direction):
                return False
        for y in range(len(grid)):
            grid[y][x] = grid[y][nx]
        return True
    return False


def solve(grid):
    r = len(grid)
    c = len(grid[0])
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '?':
                continue
            go_change(grid, j, i, "UP")
            go_change(grid, j, i, "DOWN")

    for j in range(c):
        if grid[0][j] == '?':
            copy_column(grid, j, "LEFT")
            copy_column(grid, j, "RIGHT")

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        R, C = map(int, input().split())
        cake = [list(input()) for _ in range(R)]
        solve(cake)
        ret = '\n'.join(''.join(row) for row in cake)
        print("Case #{x}:\n{y}".format(x=t, y=ret))