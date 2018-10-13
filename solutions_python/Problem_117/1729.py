from sys import stdin, stdout

def check_row(grid, row):
    for h in grid[row]:
        if h != 1:
            return False
    return True

def check_col(grid, col):
    for i in range(len(grid)):
        if grid[i][col] != 1:
            return False
    return True


def solve(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if not check_row(grid, i) and not check_col(grid, j):
                    return 'NO'

    return 'YES'


case_count = int(stdin.readline())
for i in range(case_count):
    parts = stdin.readline().split(' ')
    rows = int(parts[0])
    cols = int(parts[1])

    grid = []
    for j in range(rows):
        grid.append([int(s) for s in stdin.readline().split(' ')])

    print('Case #{}: {}'.format(i+1, solve(grid)))
