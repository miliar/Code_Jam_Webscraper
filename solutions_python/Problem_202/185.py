"""
Problem D. Fashion Show
Each cell in the grid can be empty (which we represent with a . character) or 
can contain one fashion model. The models come in three types, depending on the 
clothing style they are wearing: +, x, and the super-trendy o. A cell with 
a + or x model in it adds 1 style point to the show. A cell with an o model 
in it adds 2 style points. Empty cells add no style points.

To achieve the maximum artistic effect, there are rules on how models can be 
placed relative to each other.

Whenever any two models share a row or column, at least one of the two must 
be a +.
Whenever any two models share a diagonal of the grid, at least one of the two 
must be an x.
Formally, a model located in row i0 and column j0 and a model located in row 
i1 and column j1 share a row if and only if i0 = i1, they share a column if 
and only if j0 = j1, and they share a diagonal if and only if i0 + j0 = i1 + 
j1 or i0 - j0 = i1 - j1.

For example, the following grid is not legal:

...
x+o
.+.
The middle row has a pair of models (x and o) that does not include a +. 
The diagonal starting at the + in the bottom row and running up to the o in 
the middle row has two models, and neither of them is an x.

However, the following grid is legal. No row, column, or diagonal violates 
the rules.

+.x
+x+
o..
Your artistic advisor has already placed M models in certain cells, following 
these rules. You are free to place any number (including zero) of additional 
models of whichever types you like. You may not remove existing models, but you 
may upgrade as many existing + and x models into o models as you wish, 
as long as the above rules are not violated.

Your task is to find a legal way of placing and/or upgrading models that earns 
the maximum possible number of style points.
"""
# SCORE_MAP = {'x': 1, '+': 1, 'o': 2}

def get_small_solution(N, o_col):
    positions = dict()
    positions[(1, o_col)] = 'o'
    for col in range(1, N + 1):
        if col != o_col:
            positions[(1, col)] = '+'
    for col in range(2, N):
        positions[(N, col)] = '+'
    for col in range(2, N + 1):
        if col != o_col:
            positions[(col, col)] = 'x'
        else:
            positions[(col, 1)] = 'x'
    return positions


def solution_small(N, positions):
    # print('Original placement')
    # print_positions(N, positions)
    o_col = 1
    for pos in positions.keys():
        if pos[0] != 1:
            raise ValueError('Pre-defined position for small set should be in the first row, '
                             'but was: ' + str(pos))
        if positions[pos] != '+':
            o_col = pos[1]
    if N > 1:
        score = 3 * N - 2
        replacements = 3 * N - 3
    else:
        score = 2
        replacements = 1
    max_positions = get_small_solution(N, o_col)
    # print('Max score placement:')
    # print_positions(N, max_positions)
    for pos in positions.keys():
        if max_positions[pos] == positions[pos]:
            replacements -= 1
            del max_positions[pos]
    return score, replacements, max_positions


def print_positions(N, positions):
    grid = [[None for _ in range(N)] for _ in range(N)]
    for position, model in positions.items():
        grid[position[0] - 1][position[1] - 1] = model
    print_grid(grid)


def print_grid(grid):
    print()
    print('---' * len(grid))
    for row in grid:
        row_str = '|'
        for val in row:
            if val is not None:
                row_str += ' ' + str(val) + '|'
            else:
                row_str += '  |'
        print(row_str)
    print('---' * len(grid))
    print()



test_cases = int(input())
for i in range(1, test_cases + 1):
    input_str = input()
    N_str, M_str = input_str.split(' ')
    N = int(N_str)
    M = int(M_str)
    positions = dict()
    for _ in range(M):
        in_str = input()
        model, row_str, column_str = in_str.split(' ')
        row = int(row_str)
        column = int(column_str)
        positions[(row, column)] = model
    # print("Case #{}: N={}, M={}, positions: {}".format(i, N, M, positions))
    score, changes, max_positions = solution_small(N, positions)
    print("Case #{}: {} {}".format(i, score, changes))
    for pos, model in max_positions.items():
        print("{} {} {}".format(model, pos[0], pos[1]))

#
# def test1():
#     print(solution_small(2, {}))
#     print(solution_small(1, {(1, 1): 'o'}))
#     print(solution_small(5, {(1, 1): '+', (1, 2): 'x', (1, 3): '+', (1, 4): '+', (1, 5): '+'}))
#     print(solution_small(5, {(1, 1): '+', (1, 2): '+', (1, 3): '+', (1, 5): 'o'}))
#     print(solution_small(5, {(1, 1): '+', (1, 2): '+', (1, 3): '+', (1, 5): 'x'}))
#
# test1()