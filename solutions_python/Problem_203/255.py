def solve(r, c, lines):
    grid = [list(l) for l in lines]

    xl = []
    nc = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] != "?":
                xl += [[i, j, grid[i][j]]]
                nc += 1

    xs = 0
    ys = 0
    # print xl
    for i in range(nc):
        if i == nc - 1:
            xi, yi, ci = xl[i]
            # print xi, yi, ci
            fill(grid, xs, ys, r - 1, c - 1, ci)
            # print grid
            if ys != 0:
                copyrow(grid, xi, r, c)
        else:
            xi, yi, ci = xl[i]
            # print xi, yi, ci
            xn, yn, cn = xl[i + 1]
            # print xn, yn, cn
            if xi == xn:
                xe = xn
                ye = yn - 1
                fill(grid, xs, ys, xe, ye, ci)
                # print grid
                xs = xs
                ys = yi + 1
            else:
                xe = xn - 1
                ye = c - 1
                fill(grid, xs, ys, xe, ye, ci)
                # print grid
                xs = xi + 1
                ys = 0

    return grid


def fill(grid, xa, ya, xb, yb, c):
    for i in range(xa, xb + 1):
        for j in range(ya, yb + 1):
            grid[i][j] = c


def copyrow(grid, rn, r, c):
    for i in range(rn + 1, r):
        for j in range(c):
            grid[i][j] = grid[rn][j]


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        r, c = [int(a) for a in raw_input().split(" ")]
        lines = []
        for j in xrange(0, r):
            lines.append(raw_input())
        # if i == 73 or i == 80:
            # print lines
        sol = solve(r, c, lines)
        print "Case #{}:".format(i)
        for line in sol:
            print "".join(line)


if __name__ == "__main__":
    main()
