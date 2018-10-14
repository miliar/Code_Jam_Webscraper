import sys
import copy

def remove_column(grid, index):
    for row in grid:
        del row[index]


def minim(grid):
    return min(map(int, ''.join(''.join(row) for row in grid)))


def cut(grid):
    grid = copy.deepcopy(grid)
    for row in grid:
        r = list(set(row))
        if len(r) == 1 and int(r[0]) == minim(grid):
            grid.remove(row)
            return grid
    for i, column in enumerate(zip(*grid)):
        c = list(set(column))
        if len(c) == 1 and int(c[0]) == minim(grid):
            remove_column(grid, i)
            break
    return grid


def solve(grid):
    while True:
        new = cut(grid)
        if not new:
            return 'YES'
        elif new == grid:
            return 'NO'
        grid = new


if __name__ == '__main__':
    grids = []
    with open(sys.argv[1]) as in_:
        next(in_)
        for line in in_:
            rows = int(line.strip().split()[0])
            tmp = []
            for _ in xrange(rows):
                tmp.append(next(in_).strip().split())
            grids.append(tmp)
    with open(sys.argv[2], 'w') as out:
        for i, grid in enumerate(grids, 1):
            out.write('Case #{}: {}\n'.format(i, solve(grid)))
