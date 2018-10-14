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
from fractions import Fraction

def mk(**kwargs):
    return kwargs

def chick(num, speed, startpos, barnpos, timelimit):
    barndistance = barnpos - startpos
    bestbarntime = Fraction(barndistance, speed)
    return mk(
        num = num,
        speed = speed,
        startpos = startpos,
        bestbarntime = bestbarntime,
        can_make_it = bestbarntime <= timelimit)

def solve_case():
    num_chicks, need_saved, barnpos, timelimit = read_ints()
    chick_positions = read_ints()
    chick_speeds = read_ints()
    chicks = [
        chick(i, chick_speeds[i], chick_positions[i], barnpos, timelimit)
        for i in xrange(num_chicks)]
    can_save = [c for c in chicks if c['can_make_it']]
    #print len(can_save)
    if len(can_save) < need_saved:
        print "IMPOSSIBLE"
        return
    save_order = sorted(
        can_save,
        key=lambda c:c['startpos'],
        reverse=True)
    will_save = save_order[:need_saved]
    wont_save = save_order[need_saved:] + [
        c for c in chicks if not c['can_make_it']]
    swaps = 0
    for c1 in will_save:
        blockers = [c for c in wont_save if c['startpos'] > c1['startpos']]
        swaps += len(blockers)
    print swaps


solve_all(solve_case)
