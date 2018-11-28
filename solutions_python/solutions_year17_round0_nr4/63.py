#!/usr/bin/python
import sys
from gurobipy import *

# Gurobi can be obtained from http://www.gurobi.com/.

def solve(n, models):
    lp = Model()
    # print p
    x = lp.addVars(list(range(1, n+1)), list(range(1, n+1)), vtype=GRB.BINARY, name='x')
    o = lp.addVars(list(range(1, n+1)), list(range(1, n+1)), vtype=GRB.BINARY, name='o')
    p = lp.addVars(list(range(1, n+1)), list(range(1, n+1)), vtype=GRB.BINARY, name='p')
    for i in range(1, n+1):
        for j in range(1, n+1):
            lp.addConstr(x[(i, j)] + o[(i, j)] + p[(i, j)] <= 1)
        # Row constraints
        lp.addConstr(sum(x[i, j] + o[i, j] for j in range(1, n+1)) <= 1)
        lp.addConstr(sum(x[j, i] + o[j, i] for j in range(1, n+1)) <= 1)
    # Diagonal constraints 
    for d in range(1-n, n):
        lp.addConstr(sum(o[r, r - d] + p[r, r - d]
                              for r in range(1, n+1) if 1 <= r - d <= n) <= 1)
        
    for d in range(2, 2*n+1):
        lp.addConstr(sum(o[r, d - r] + p[r, d - r]
                              for r in range(1, n+1) if 1 <= d - r <= n) <= 1)
    # Models constraints
    for (r, c), v in models.items():
        if v == 'o':
            lp.addConstr(o[(r, c)] == 1)
        elif v == 'x':
            lp.addConstr(o[(r, c)] + x[(r, c)] == 1)
        else:
            # Must be '+'.
            lp.addConstr(o[(r, c)] + p[(r, c)] == 1)
    # Objective
    objective = 2 * sum(o[(i, j)]
                        for i in range(1, n+1)
                        for j in range(1, n+1)) + \
                sum(x[(i, j)] + p[(i, j)]
                    for i in range(1, n+1)
                    for j in range(1, n+1))
    lp.setObjective(objective, GRB.MAXIMIZE)
    # lp.write_lp('test.lp')
    lp.setParam('OutputFlag', False)
    lp.setParam('Threads', 4)
    lp.optimize()
    ans = lp.objVal
    x = lp.getAttr('x', x)
    o = lp.getAttr('x', o)
    p = lp.getAttr('x', p)
    sol = {}
    for i in range(1, n+1):
        for j in range(1, n+1):
            if x[(i, j)] == 1:
                sol[(i, j)] = 'x'
            elif p[(i, j)] == 1:
                sol[(i, j)] = '+'
            elif o[(i, j)] == 1:
                sol[(i, j)] = 'o'
    return sol, int(ans + 0.1)

n_cases = int(sys.stdin.readline())
for i in range(1, n_cases+1):
    n, m = map(int, sys.stdin.readline().split())
    d = dict()
    for j in range(m):
        t, r, c = sys.stdin.readline().split()
        r, c = int(r), int(c)
        d[(r, c)] = t
    w, score = solve(n, d)
    mods = []
    for (r, c), v in w.items():
        if (r, c) not in d:
            mods.append((v, r, c))
        elif d[(r, c)] != v:
            mods.append((v, r, c))
    print 'Case #{0}: {1} {2}'.format(i, score, len(mods))
    for v, r, c in mods:
        print v, r, c
