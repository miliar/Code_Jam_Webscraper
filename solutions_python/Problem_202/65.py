from collections import defaultdict
import multiprocessing

from pulp import *

f = [sys.stdin]


def replace_stdin():
    print("WARNING! replacing stdin")
    sys.stderr.write("WARNING! replacing stdin\n")
    f[0] = open('in', 'r')


# replace_stdin()

def ln():
    return f[0].readline().strip()

class LinName(object):
    def __init__(self, base):
        self.base = base
        self.n = 0

    def __call__(self, *args, **kwargs):
        self.n += 1
        return self.base + str(self.n)

class Vars(object):
    def __init__(self, n):
        self._all_coords = [
            (t, r, c)
            for r in range(n)
            for c in range(n)
            for t in '+xo']
        self.vars = {k: LpVariable(self.name(*k), 0, 1, LpInteger) # WARNING TODO!!!
                     for k in self.allCoords()}

    def get(self, type, row, col):
        return [self.vars[(t, row, col)]
                for t in type]

    def abstrClassVars(self, type, abstrClassPred):
        group = defaultdict(list)
        for t, r, c in self.allCoords():
            if t not in type:
                continue
            v = self.vars[(t,r,c)]
            group[abstrClassPred(r,c)].append(v)
        return group.values()

    def allCoords(self):
        return self._all_coords

    def addCellConstraints(self, prob):
        nextName = LinName("CellMutexConstr")
        for group in self.abstrClassVars('+xo', lambda r, c: r * 10**3+c):
            prob += lpSum(group) <= 1, nextName()

    def allVars(self, type):
        return self.abstrClassVars(type, lambda r,c: 0)

    def name(self, type, row, col):
        return "%s_%d_%d" % ('p' if type == '+' else type, row, col)


def solve(n, customs, save_name):
    # Create the 'prob' variable to contain the problem data
    prob = LpProblem("D Problem", LpMinimize)

    v = Vars(n)
    prob += -((lpSum(v.allVars('x+')) + 2 * lpSum(v.allVars('o'))))

    v.addCellConstraints(prob)

    limitedClasses = (v.abstrClassVars('xo', lambda row, col: row) +
                      v.abstrClassVars('xo', lambda row, col: col) +
                      v.abstrClassVars('+o', lambda row, col: row - col) +
                      v.abstrClassVars('+o', lambda row, col: row + col))

    nextName = LinName("RowColDiagConstr")
    for xoClass in limitedClasses:
        prob += lpSum(xoClass) <= 1, nextName()

    nextName = LinName("CustomsConstr")
    for type, row, col in customs:
        typeFilt = {'x': 'xo', '+': '+o', 'o': 'o'}[type]
        prob += lpSum(v.get(typeFilt, row, col)) >= 1, nextName()

    prob.writeLP("%s.lp" % (save_name,))

    prob.solve(solver=COIN_CMD())

    sys.stderr.write("Status: " + LpStatus[prob.status] + "\n")

    finalSetup = set()
    for type, row, col in v.allCoords():
        if v.get(type, row, col)[0].varValue >= 0.9:
            finalSetup.add((type, row, col))

    return -value(prob.objective), finalSetup

def solve_args(args):
    return solve(*args)


def solve_codejam():
    tests = int(ln())
    inputs = []
    for test_nr in range(1, tests + 1):
        N, M = map(int, ln().split())
        customs = []
        for _ in range(M):
            type, row, col = ln().split()
            row, col = map(lambda s: int(s)-1, (row, col))
            customs.append((type, row, col))

        inputs.append((N, customs, 'Case%d' % test_nr))

    pool = multiprocessing.Pool(16)

    results = pool.map(solve_args, inputs)
    for i, (opt_val, setup) in enumerate(results):
        setup -= set(inputs[i][1])
        print("Case #%d: %d %d" % (i+1, opt_val, len(setup)))
        for t, r, c in setup:
            print t, r+1, c+1

solve_codejam()


