def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        r, c = [int(s) for s in raw_input().split(" ")]
        grid = [list(raw_input()) for _ in range(r)]

        print "Case #{}:".format(i)
        solve(grid)


def solve(grid):
    b = [any(c != '?' for c in r) for r in grid]
    row = []
    lastr = None
    for i, r in enumerate(grid):
        if b[i]:
            col = []
            lastc = None
            for j, c in enumerate(r):
                if c == '?' and lastc is None:
                    col.append(j)
                elif c == '?':
                    r[j] = lastc
                else:
                    for k in col:
                        r[k] = c
                    col = []
                    lastc = c
            for k in row:
                for j in range(len(r)):
                    grid[k][j] = r[j]
            row = []
            lastr = r
        else:
            if lastr is None:
                row.append(i)
            else:
                for j in range(len(lastr)):
                    r[j] = lastr[j]

    for r in grid:
        print ''.join(r)



if __name__=='__main__':
    main()