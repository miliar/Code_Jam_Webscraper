from sys import argv


def get_col(grid, j):
    col = ''
    for i in range(4):
        col += grid[i][j]
    return col


def get_diags(grid):
    diag1 = ''
    for i in range(4):
        diag1 += grid[i][i]
    diag2 = ''
    for i in range(4):
        diag2 += grid[i][3-i]
    return [diag1, diag2]


X_WINS = [set('X'), set('XT')]
O_WINS = [set('O'), set('OT')]

def is_win_for(line):
    line = set(line)
    if line in X_WINS:
        return 'X'
    if line in O_WINS:
        return 'O'
    return None


def check_grid(grid, test_num):
    lines = grid + [get_col(grid, i) for i in range(4)] + get_diags(grid)
    for l in lines:
        winner = is_win_for(l)
        if winner:
            print 'Case #%d: %s won' % (test_num, winner)
            return
    for r in grid:
        if '.' in r:
            print 'Case #%d: Game has not completed' % test_num
            return
    print 'Case #%d: Draw' % test_num


in_fname = argv[1]
f = open(in_fname)

T = int(f.readline().strip())
for it in range(T):
    grid = []
    for il in range(0, 4):
        row = f.readline().strip()
        grid.append(row)
    f.readline()
    check_grid(grid, it+1)

