#!/usr/bin/env python3

import sys

def solve(grid, R, C):
    grid = [list(row) for row in grid]

    empty_rows = []
    good_rows = []

    # try to fill in horizontals? (greedy)
    for r in range(R):
        first_c = 0
        while first_c < C and grid[r][first_c] == '?':
            first_c += 1

        # didn't find first_c
        if first_c == C:
            empty_rows.append(r)
            continue
        else:
            good_rows.append(r)

        # fill in before first_c
        for c in range(first_c):
            grid[r][c] = grid[r][first_c]

        # fill in the rest
        last_c = first_c
        for c in range(first_c + 1, C):
            if grid[r][c] == '?':
                grid[r][c] = grid[r][last_c]
            else:
                last_c = c

        assert all(e != '?' for e in grid[r])


    print('empty rows:', empty_rows, file=sys.stderr)

    # copy rows into empty rows
    last_good_row = 0
    for r in empty_rows:
        if r < good_rows[0]:
            grid[r] = grid[good_rows[0]]
        else:
            while last_good_row + 1 < len(good_rows) and \
                    r > good_rows[last_good_row + 1]:
                last_good_row += 1
            grid[r] = grid[good_rows[last_good_row]]


    res = '\n'.join(''.join(row) for row in grid)
    assert res.find('?') == -1

    print('OUTPUT:', file=sys.stderr)
    print(res, file=sys.stderr)
    return res


T = int(input())
for t in range(T):
    r, c = map(int, input().split())
    grid = [input() for _ in range(r)]

    print(file=sys.stderr)
    print('Case #{}:'.format(t+1), file=sys.stderr)
    print('INPUT', file=sys.stderr)
    print('\n'.join(grid), file=sys.stderr)

    res = solve(grid, r, c)
    print('Case #{}:\n{}'.format(t+1, res))

