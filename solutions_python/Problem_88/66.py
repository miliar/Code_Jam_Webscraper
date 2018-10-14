def works(grid, corner, k):
    x,y = corner
    cx, cy = x + (k-1)/2., y + (k-1)/2.
    wx = 0
    wy = 0
    exclude = [(x, y), (x, y+k-1), (x+k-1, y), (x+k-1, y+k-1)]
    for i in range(x, x+k):
        for j in range(y, y + k):
            if (i, j) in exclude:
                continue
            d = grid[i][j]
            dx = (i - cx)* d
            dy = (j - cy)* d
            wx += dx
            wy += dy
    return abs(wx) <= 10**-10 and abs(wy) <= 10**-10

def solve(grid, R, C, D):
    for i in range(R):
        for j in range(C):
            grid[i][j] += D
    max_k = min(R, C)
    for k in range(max_k, 2, -1):
        for i in range(R):
            for j in range(C):
                corner = (i, j)
                if i + k > R or j+k > R:
                    continue
                if works(grid, corner, k):
                    return k
    return False

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        R, C, D = map(int, raw_input().split())
        grid = []
        for j in range(R):
            grid.append(map(int, list(raw_input())))
        k = solve(grid, R, C, D)
        print "Case #%d:" % i,
        if k:
            print k
        else:
            print "IMPOSSIBLE"

