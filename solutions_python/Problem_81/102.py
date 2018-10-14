# Dougall Johnson, May 22 2011
import sys
def read_ints(): return map(int, raw_input().split(" "))
def to_ints(s): return map(int, s.split(" "))

def calc_win_percents(grid):
    l = []
    for row in grid:
        wp = float(row.count('1'))/(row.count('1')+row.count('0'))
        l.append(wp)
    return l

def calc_owp(grid):
    l = []
    for i, row in enumerate(grid):
        opponents = []
        for j, v in enumerate(row):
            if v in "01":
                opponents.append(j)
        owps = []
        for o in opponents:
            r = grid[o]
            r = r[:i] + r[i+1:]
            owps.append(float(r.count('1'))/(r.count('1')+r.count('0')))
        l.append(sum(owps)/len(owps))
    return l

def calc_oowp(grid, owps):
    l = []
    for i, row in enumerate(grid):
        opponents = []
        for j, v in enumerate(row):
            if v in "01":
                opponents.append(j)
        oowps = []
        for o in opponents:
            oowps.append(owps[o])
        l.append(sum(oowps)/len(oowps))
    return l

def solve(num_teams, grid):
    wp = calc_win_percents(grid)
    owp = calc_owp(grid)
    oowp = calc_oowp(grid, owp)
    l = []
    for a, b, c in zip(wp, owp, oowp):
        l.append(0.25*a+0.5*b+0.25*c)
    return l

num_problems, = read_ints()
for i in range(num_problems):
    num_teams, = read_ints()
    grid = [raw_input() for j in range(num_teams)]
    print "Case #%i:" % (i+1)
    print "\n".join(repr(f) for f in solve(num_teams, grid))


#data = "".join(sys.stdin.readlines()).strip()
