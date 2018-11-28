# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.


def run(grid, n, m):
    """
    idea: allocate row first then columns
    :param grid: 
    :param n: 
    :param m: 
    :return: 
    """

    # find first row
    for r in range(n):
        first_r = r
        row = grid[r]
        if any([a!='?' for a in row]):
            last_rv = row
            break

    for r in range(first_r, n):
        row = grid[r]
        for c in range(m):
            first_c = c
            first_cv = row[first_c]
            last_cv = row[first_c]
            if row[first_c]!='?':
                break

        if first_cv == '?':
            # empty line
            grid[r] = last_rv
            continue

        for c in range(first_c):
            grid[r][c] = first_cv

        for c in range(first_c, m):
            if grid[r][c] == '?':
                grid[r][c] = last_cv
            else:
                last_cv = grid[r][c]
        last_rv = grid[r]

    for r in range(first_r):
        grid[r] = grid[first_r]

    return grid



t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
    #print(input())
    n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    grid = []
    for r in range(n):
        row = raw_input()
        grid.append(list(row))


    print("Case #{}:".format(i))
    #for r in range(n):
    #    print ''.join(map(str, grid[r]))
    new_grid = run(grid, n, m)
    for r in range(n):
        print ''.join(map(str, grid[r]))

    #print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting option

