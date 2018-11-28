def min_unhappy(grid, R, C, n, offset = 0):
    u = 0
    if n == 0:
        for i in range(R):
            for j in range(C):
                x = i * C + j
                y = i * C + j + 1
                z = (i+1) * C + j
                if not grid[x]:
                    continue
                if (j+1) % C != 0 and grid[y]:
                    u += 1
                if (i+1) % R != 0 and grid[z]:
                    u += 1
        return u

    if offset + n == R * C:
        return min_unhappy(grid[:offset] + [True] * n, R, C, 0, offset+n)

    g1 = grid[:offset] + [True] + [False] * (R*C-offset)
    g2 = grid[:offset] + [False] + [False] * (R*C-offset)
    return min(min_unhappy(g1, R, C, n-1, offset+1), min_unhappy(g2, R, C, n, offset+1))
    
if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        R,C,N = map(int, raw_input().split())
        print "Case #%d: %d" % (i, min_unhappy([False]*(R*C), R, C, N))
