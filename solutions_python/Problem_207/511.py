#!/usr/bin/python2

import sys
from gurobipy import *

def solve(N, R, O, Y, G, B, V):
    lp = Model()
    e = lp.addVars(['ry', 'rb', 'yb'], vtype=GRB.INTEGER, name='e')
    
    # Constraints
    lp.addConstr(2 * B == e['rb'] + e['yb'])
    lp.addConstr(2 * R == e['ry'] + e['rb'])
    lp.addConstr(2 * Y == e['yb'] + e['ry'])
    lp.addConstr(e['ry'] >= 0)
    lp.addConstr(e['rb'] >= 0)
    lp.addConstr(e['yb'] >= 0)
    
    # Objective
    objective = 1
    lp.setObjective(objective, GRB.MAXIMIZE)
    
    lp.setParam('OutputFlag', False)
    lp.setParam('Threads', 4)
    lp.optimize()
    
    try:
        sol = lp.getAttr('x', e)
        # print(sol)
        yb = int(sol['yb'] + 0.1)
        ry = int(sol['ry'] + 0.1)
        rb = int(sol['rb'] + 0.1)
        sol = 'R' if R > 0 else ('Y' if Y > 0 else 'B')
        while yb + ry + rb > 0:
            if sol[-1] == 'R':
                if ry > rb:
                    sol += 'Y'
                    ry -= 1
                else:
                    rb -= 1
                    sol += 'B'
            elif sol[-1] == 'B':
                if rb > yb:
                    sol += 'R'
                    rb -= 1
                else:
                    yb -= 1
                    sol += 'Y'
            else:  # sol[-1] == 'Y'
                if ry > yb:
                    ry -= 1
                    sol += 'R'
                else:
                    yb -= 1
                    sol += 'B'
            
        # print(sol)
        sol = sol[:-1]
        return sol
    except gurobipy.GurobiError:
        return 'IMPOSSIBLE'
    
n_cases = int(sys.stdin.readline())

for i in range(1, n_cases+1):
    N, R, O, Y, G, B, V = map(int, sys.stdin.readline().split())
    sol = solve(N, R, O, Y, G, B, V)
    if sol != 'IMPOSSIBLE':
        assert sol.count('R') == R
        assert sol.count('Y') == Y
        assert sol.count('B') == B
        assert len(sol) == N
        assert sol[0] != sol[-1]
    # if sol == 'IMPOSSIBLE':
    print 'Case #{0}: {1}'.format(i, sol)
