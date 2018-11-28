def solve(R, C, D, grid):
    best = 0
    for K in range(3, min(R, C) + 1):
        for i0 in range(R - K + 1):
            for j0 in range(C - K + 1):
                ci, cj = i0 + (K - 1) / 2, j0 + (K - 1) / 2
                corners = {(i0, j0), (i0, j0 + K - 1), (i0 + K - 1, j0), (i0 + K - 1, j0 + K - 1)}
                mi = sum((i - ci) * grid[i][j] for i in range(i0, i0 + K) for j in range(j0, j0 + K) if (i, j) not in corners)
                mj = sum((j - cj) * grid[i][j] for i in range(i0, i0 + K) for j in range(j0, j0 + K) if (i, j) not in corners)
                #if K == 5 and i0 == 1 and j0 == 1: print(ci, cj, mi, mj)
                if mi == 0 and mj == 0:
                    best = K
    return best if best > 0 else "IMPOSSIBLE"

def main():
    T = int(input())
    for i in range(1, T + 1):
        R, C, D = map(int, input().split())
        grid = [list(map(int, input().strip())) for i in range(R)]
        ans = solve(R, C, D, grid)
        print('Case #%d: %s' % (i, ans))

if __name__ == '__main__':
    main()

