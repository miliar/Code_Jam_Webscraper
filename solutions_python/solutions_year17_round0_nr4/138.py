# place o so they don't share diagonals or rows (queens)
# fill with +?
# fill with x?

# exhaustive search
# if there's a contradiction, return nothing
# otherwise, 
#   if it's the last square + 1 return the history
#   else, return the result of extending the history with all 4 possibilities

from copy import deepcopy
from collections import namedtuple
import functools

def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer

Grid_ = namedtuple('Grid', 'cells N')

class Grid(Grid_):
        __slots__ = ()
        def __str__(self):
            return show(self) + ' score=' + str(score(self))
        def __eq__(self, other):
            if self.N != other.N:
                return False
            for i in range(self.N):
                for j in range(self.N):
                    if self.cells[i][j] != other.cells[i][j]:
                        return False
            return True

style_points = {'x': 1, '+': 1, 'o': 2, '.': 0}
legal_substitutions_dict = {'.': '+xo', '+': 'o', 'x': 'o', 'o': ''}
legal_substitutions = [a + c for a,s in legal_substitutions_dict.items() 
                             for c in s]

queen_substitutions_dict = {'.': 'o', 'o': ''}

@memoize
def index_ij(N):
    return [(i, j) for i in range(N) for j in range(N)]

@memoize
def row_at(N, i):
    row = i / N
    return [(i_, j_) for (i_, j_) in index_ij(N) if i_ == row]

@memoize
def col_at(N, i):
    col = i % N
    return [(i_, j_) for (i_, j_) in index_ij(N) if j_ == col]

@memoize
def diags_at(N, i):
    row, col = i / N, i % N
    a, b = row + col, row - col
    diags = ([(i_, j_) for (i_, j_) in index_ij(N) 
                    if (i_ + j_ == a)]
            ,[(i_, j_) for (i_, j_) in index_ij(N) 
                    if (i_ - j_ == b)])
    return diags

def show(grid):
    output = []
    for row in grid.cells:
        output += [''.join(row)]
    return '\n'.join(output)

def to_grid(N, entries):
    cells = [['.' for _ in range(N)] for _ in range(N)]
    for m,i,j in entries:
        cells[i][j] = m
    return Grid(cells, N)

def parse(text):
    lines = iter(l for l in text.split('\n') if l)
    n = int(lines.next())
    arr = []

    for line in lines:
        N, M = line.split()
        N, M = int(N), int(M)

        entries = []
        for _, line in zip(range(M), lines):
            m, i, j = line.split()
            i, j = int(i) - 1, int(j) - 1
            entries += [[m, i, j]]
        arr += [[N, entries]]

    return arr


    Ns = [int(s) for s in lines[1:] if s != '']
    assert n == len(Ns)
    return Ns

def load(f):
    grids = [to_grid(N, entries) for N, entries in parse(open(f).read())]
    return grids

def cell_at(grid, i):
    i_, j_ = i / grid.N, i % grid.N
    return grid.cells[i_][j_]

def set_cell_at(grid, i, value):
    i_, j_ = i / grid.N, i % grid.N
    grid.cells[i_][j_] = value

def contradiction_at(grid, i):
    row  = row_at(grid.N, i)
    col  = col_at(grid.N, i) 
    diagA, diagB = diags_at(grid.N, i)
    
    def multiple(letters, coords):
        flag = 0
        for (i,j) in coords:
            flag += grid.cells[i][j] in letters
            if flag > 1:
                return True
        return False

    return (multiple('xo', row)   or 
            multiple('xo', col)   or
            multiple('+o', diagA) or
            multiple('+o', diagB))

def contradiction(grid):
    top_row = range(grid.N)
    left_col = [x*grid.N for x in top_row] 
    for i in top_row + left_col:
        if contradiction_at(grid, i):
            return True
    return False

def score(grid):
    return sum([style_points[cell] for row in grid.cells for cell in row])

#########

def output(original_grid, final_grid, case):
    # case must be 1-indexed already
    assert original_grid.N == final_grid.N
    N = original_grid.N

    entries = []
    for i in range(N):
        for j in range(N):
            a = original_grid.cells[i][j]
            b = final_grid.cells[i][j]
            if a != b:
                assert (a + b) in legal_substitutions
                entries += [(b, i + 1, j + 1)]

    header = 'Case #%d: %d %d' % (case, score(final_grid), len(entries))
    entries = ['%s %d %d' % e for e in entries]

    return '\n'.join([header] + entries)

def extend(grid, i, sub_dict=legal_substitutions_dict):
    # extend the NxN grid at position i
    # return a list of new grids
    # should we also pass on a list of candidates
    # and eliminate 
    start = cell_at(grid, i)
    ends = sub_dict[start]
    grids = [grid]
    for end in ends:
        g = deepcopy(grid)
        set_cell_at(g, i, end)
        if not contradiction_at(g, i):
            grids += [g]
    return grids

def extender(grids, i, sub_dict=legal_substitutions_dict):
    if len(grids) == 0:
        return grids
    if i >= grids[0].N * grids[0].N:
        return grids
    # concatMap
    new_grids = [g2 for g in grids for g2 in extend(g, i, sub_dict=sub_dict)]
    return extender(new_grids, i+1, sub_dict=sub_dict)

def extender_once(grids, i, sub_dict=legal_substitutions_dict):
    if len(grids) == 0:
        return grids
    if i >= grids[0].N * grids[0].N:
        return grids
    # concatMap
    for g in grids:
        new_grids = extend(g, i, sub_dict=sub_dict)

    new_grids = [g2 for g in grids for g2 in extend(g, i, sub_dict=sub_dict)]
    return extender(new_grids, i+1, sub_dict=sub_dict)

def solve_queens(N):
    grid = to_grid(N, [])
    solutions = extender([grid], 0, sub_dict=queen_substitutions_dict)
    return [g for g in solutions if score(g) == N*2]

def maximize(grid, all_best=False):
    solutions = extender([grid], 0)
    scores = [score(g) for g in solutions]
    
    if all_best:
        return [g for g in solutions if score(g) == max(scores)]

    best = scores.index(max(scores))
    return solutions[best]

def canonicalize(row):
    # upgrade x to o
    # if there is no o, make the first entry o (. -> o or + -> o)
    # replace all . with +
    row = list(row)
    if 'x' in row:
        row[row.index('x')] = 'o'
        return canonicalize(row)
    if 'o' not in row:
        row[0] = 'o'
        return canonicalize(row)
    row = ['+' if c == '.' else c for c in row]
    return row

def z_solution(N):
    """
    >>> print z_solution(4)
    o+++
    .x..
    ..x.
    .++x score=10
    """
    grid = to_grid(N, [])
    header = ['o'] + ['+'] * (N - 1)
    grid.cells[0] = header
    for i in range(1,N):
        grid.cells[N - 1][i] = '+'
        grid.cells[i][i] = 'x'   
    return grid 

def transpose(grid):
    grid = deepcopy(grid)
    cells_T = zip(*grid.cells)
    for i in range(grid.N):
        for j in range(grid.N):
            grid.cells[i][j] = cells_T[i][j]
    return grid

def mirror_LR(grid):
    return transpose(mirror_UD(transpose(grid)))

def mirror_UD(grid):
    grid2 = deepcopy(grid)
    grid2.cells.reverse()
    return grid2

def z_reorder(grid, o_col):
    # assume o starts off in top left
    grid = transpose(grid)
    cells_reorder =  ([grid.cells[i] for i in range(1,o_col+1)] +
                      [grid.cells[0]] +
                      [grid.cells[i] for i in range(o_col+1, grid.N)])
    for i in range(grid.N):
        grid.cells[i] = cells_reorder[i]
    
    # don't move the + in the bottom row
    a = grid.cells[0][-1]
    b = grid.cells[o_col][-1]
    grid.cells[0][-1] = b
    grid.cells[o_col][-1] = a

    return transpose(grid)

def z_solver(row):
    N = len(row)
    row = canonicalize(row)
    o_col = row.index('o')
    z_grid = z_solution(N)
    # special case
    if o_col == N - 1:
        return mirror_LR(z_grid)

    grid = z_reorder(z_grid, o_col)

    return grid

def test_z_solver(N):
    import random
    rows = []
    for _ in range(100):
        row = [random.choice('.+xo') for _ in range(N)]
        if len([_ for c in row if c in 'xo']) < 2:
            # ok
            rows += [row]

    tests = 0
    for row in rows:
        grid = to_grid(N, [])
        grid.cells[0] = list(row)
        solutions = maximize(grid, all_best=True)

        grid2 = z_solver(row)
        assert grid2 in solutions
        tests += 1

    print 'passed %d tests' % tests
    
def run_z_solver(f):
    grids = load(f)
    lines = []
    for i, grid in enumerate(grids):
        row = grid.cells[0]
        grid2 = z_solver(row)
        lines += [output(grid, grid2, i+1)]

    f2 = f + '.out'
    txt = '\n'.join(lines) + '\n'
    with open(f2, 'w') as fh:
        fh.write(txt)
    print 'wrote output to', f2



example_input = \
"""3
2 0
1 1
o 1 1
3 4
+ 2 3
+ 2 1
x 3 1
+ 2 2
"""

example_input_grids = [to_grid(*args) for args in parse(example_input)]

example_output = \
"""Case #1: 4 3
o 2 2
+ 2 1
x 1 1
Case #2: 2 0
Case #3: 6 2
o 2 3
x 1 2
"""