# Python 3.5.1

from common import *

def main(casenum):
    n, m = readints()
    grid = [['.' for i in range(n)] for j in range(n)]
    xrow = []
    xcol = []

    for i in range(m):
        t, r, c = readline().split()
        r = int(r)
        c = int(c)
        grid[r - 1][c - 1] = t
        if t == 'x' or t == 'o':
            xrow.append(r)
            xcol.append(c)

    if n == 1:
        if grid[0][0] == 'o':
            writecase(casenum, '2 0')
        else:
            writecase(casenum, '2 1')
            writeline('o 1 1')
        return

    changes = []
    # Add xs
    while len(xrow) < n:
        i = 1
        while i in xrow:
            i += 1
        j = 1
        while j in xcol:
            j += 1
        xrow.append(i)
        xcol.append(j)

        if i == 1:
            changes.append('o {} {}'.format(i, j))
            grid[i - 1][j - 1] = 'o'
        elif i == n and j > 1 and j < n:
            changes.append('o {} {}'.format(i, j))
            grid[i - 1][j - 1] = 'o'
        else:
            changes.append('x {} {}'.format(i, j))
            grid[i - 1][j - 1] = 'x'

    # Add +s
    for j in range(1, n + 1):
        t = grid[0][j - 1]
        if t == '.':
            changes.append('+ {} {}'.format(1, j))
        elif t == 'x':
            changes.append('o {} {}'.format(1, j))
    for j in range(2, n):
        t = grid[n - 1][j - 1]
        if t == '.':
            changes.append('+ {} {}'.format(n, j))
        elif t == 'x':
            changes.append('o {} {}'.format(n, j))

    writecase(casenum, '{} {}'.format(3 * n - 2, len(changes)))
    for change in changes:
        writeline(change)

run(main)
