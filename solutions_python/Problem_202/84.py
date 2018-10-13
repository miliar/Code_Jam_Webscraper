import numpy as np
# from matplotlib import pyplot as plt

def place_rooks(grid):

    n = grid.shape[0]

    new_rooks = []
    row_sum = grid.sum(axis=1)
    col_sum = grid.sum(axis=0)

    for i in range(n):
        if row_sum[i]:
            continue

        for j in range(n):
            if col_sum[j]:
                continue

            new_rooks += [(i, j)]
            grid[i, j] = True
            row_sum[i] += 1
            col_sum[j] += 1

            break

    return grid, new_rooks


def place_bishop(i_new, j_new, free):
    n = free.shape[0]

    offset_pos = j_new - i_new
    offset_neg = j_new + i_new

    for i in range(0, n):
        j = offset_pos + i
        if 0 <= j and j < n:
            free[i, j] = False

        j = offset_neg - i
        if 0 <= j and j < n:
            free[i, j] = False

    return free


def place_bishops(grid, bishops):

    n = grid.shape[0]

    free = np.ones((n, n)).astype(bool)

    for (i_bishop, j_bishop) in bishops:
        free = place_bishop(i_bishop, j_bishop, free)

    new_bishops = []
    while np.any(free):
        cost_opt = float('inf')
        i_opt = None
        j_opt = None
        for i, j in zip(*np.where(free)):
            cost_i = min(i, n - i - 1)
            cost_j = min(j, n - j - 1)
            cost = min(cost_i, cost_j)
            if cost < cost_opt:
                cost_opt = cost
                i_opt = i
                j_opt = j

        new_bishops += [(i_opt, j_opt)]
        grid[i_opt, j_opt] = True
        free = place_bishop(i_opt, j_opt, free)

    # print(grid)
    # print(free)
    # print('-'*50)

    # plt.imshow(grid, cmap='gray')
    # plt.show()

    return grid, new_bishops

if __name__=='__main__':
    PATH_IN = 'D-large.in'
    PATH_OUT = PATH_IN[:-3] + '.out'

    f_in = open(PATH_IN, 'r')
    f_out = open(PATH_OUT, 'w')

    T = int(f_in.readline())
    for t in range(T):
        line = f_in.readline().split()
        print(line)

        N = int(line[0])
        M = int(line[1])

        rook_grid = np.zeros((N, N)).astype(bool)
        bishop_grid = np.zeros((N, N)).astype(bool)
        bishops = []

        for _ in range(M):
            line = f_in.readline().split()
            print(line)

            c = line[0]
            i = int(line[1]) - 1
            j = int(line[2]) - 1

            if c in ['o', 'x']:
                rook_grid[i, j] = True
            if c in ['o', '+']:
                bishop_grid[i, j] = True
                bishops += [(i, j)]

        rook_grid, new_rooks = place_rooks(rook_grid)
        bishop_grid, new_bishops = place_bishops(bishop_grid, bishops)

        score = rook_grid.sum() + bishop_grid.sum()

        new_models = set()
        for (i, j) in new_rooks:
            if bishop_grid[i, j]:
                new_models.add(('o', i, j))
            else:
                new_models.add(('x', i, j))
        for (i, j) in new_bishops:
            if rook_grid[i, j]:
                new_models.add(('o', i, j))
            else:
                new_models.add(('+', i, j))

        print('Case #%i: %i %i' % (t+1, score, len(new_models)))
        print()
        f_out.write('Case #%i: %i %i\n' % (t+1, score, len(new_models)))
        for (c, i, j) in new_models:
            f_out.write('%s %i %i\n' % (c, i+1, j+1))

