# MISC
read_int = lambda:int(raw_input().strip())
read_ints = lambda:[int(x) for x in raw_input().split()]
count_to = lambda n:xrange(1,n+1)

# GENERAL GRID TOOLS
def read_grid(rows, columns, parse_cell=None):
    if parse_cell is None:
        parse_cell = lambda x:x
    grid = {}
    for r in count_to(rows):
        rowstring = raw_input()
        for c in count_to(columns):
            grid[r,c] = parse_cell(rowstring[c-1])
    return grid

def print_grid(rows, columns, grid, f=None):
    if f is None:
        f = lambda x:x
    for r in count_to(rows):
        print "".join(f(grid[r,c]) for c in count_to(columns))

def create_grid(rows, columns, f):
    return dict(
        ((r,c), f(r,c))
        for r in count_to(rows)
        for c in count_to(columns))

# GENERAL SOLVE LOOP
def solve_all(solve):
    num_cases = read_int()
    for i in count_to(num_cases):
         print "Case #{0}:".format(i),
         solve()

# SOLUTION
def expand_parents(dirname):
    components = dirname.split('/')[1:]
    for i in xrange(len(components)):
        yield ''.join('/'+components[j] for j in xrange(i+1))

def solve_case():
    n, m = read_ints()
    have_dirs = set(raw_input().strip() for i in xrange(n))
    need_dirs = set()
    for i in xrange(m):
        need_dirs.update(expand_parents(raw_input().strip()))
    print len(need_dirs - have_dirs)

solve_all(solve_case)
