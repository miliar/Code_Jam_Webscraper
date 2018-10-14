import sys

def solve(grid):
    nRows = len(grid)
    nCols = len(grid[0])

    for r in range(nRows):
        for c in range(nCols):
            letter = grid[r][c]
            if letter == '?':
                continue
            working_grid = grid
            bottom_grid = []
            right_grid = []
            for split_row in range(r+1, nRows):
                if any(l != '?' for l in grid[split_row]):
                    working_grid = grid[:split_row]
                    bottom_grid = solve(grid[split_row:])
                    break
            for split_col in range(c+1, nCols):
                if any(working_grid[_r][split_col] != '?' for _r in range(len(working_grid))):
                    right_grid = solve([working_row[split_col:] for working_row in working_grid])
                    working_grid = [working_row[:split_col] for working_row in working_grid]
                    break
            working_grid = [[letter for _c in range(len(working_grid[0]))] for _r in range(len(working_grid))]
            #print working_grid
            #print ''
            #print right_grid
            #print ''
            #print bottom_grid
            #print ''
            #print grid
            #print ''
            if right_grid:
                assert len(working_grid[0]) + len(right_grid[0]) == len(grid[0])
            else:
                assert len(working_grid[0]) == len(grid[0])
            if right_grid:
                for i, t in enumerate(zip(working_grid, right_grid)):
                    working_row, right_row  = t
                    working_grid[i] = working_row + right_row
            return working_grid + bottom_grid
    assert False


t = int(next(sys.stdin))
for test in range(t):
    r, c = [int(s) for s in next(sys.stdin).strip().split(' ')]
    g = [list(next(sys.stdin).strip()) for _ in range(r)]
    print('Case #{}:'.format(test+1))
    print('\n'.join(''.join(row) for row in solve(g)))
