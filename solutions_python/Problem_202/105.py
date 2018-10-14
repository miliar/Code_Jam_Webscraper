import sys
import random
import re
import itertools
import math
import copy
import bisect
import Queue
from collections import Counter
from multiprocessing import Pool
from pulp import *

verbose = False


def read():
    # *only* read data for a single test case
    n, m = [int(u) for u in sys.stdin.readline().split()]
    models = []
    for i in xrange(m):
        t, r, c = sys.stdin.readline().split()
        r = int(r)
        c = int(c)
        models.append((t, r, c))
    
    return n, m, models


def write(res):
    # write answer for a single test case
    points, changed = res
    print points, len(changed)
    for (t,r,c) in changed:
        print t, r, c


def solve(data):
    n, m, models = data
    
    TYPES = ['+', 'x', 'o']
    VALUE = {
        '+': 1,
        'x': 1,
        'o': 2,
    }
    
    prob = LpProblem("myProblem", LpMaximize)
    
    variables = {(t,r,c): LpVariable("%s,%d,%d" % (t,r,c), lowBound=0, upBound=1, cat="Integer") for t in TYPES for r in xrange(1, n+1) for c in xrange(1, n+1)}
    
    # at most one model per cell
    for r in xrange(1, n+1):
        for c in xrange(1, n+1):
            prob += lpSum(variables[(t,r,c)] for t in TYPES) <= 1
    
    # rows
    for r in xrange(1, n+1):
        prob += lpSum(variables[(t,r,c)] for c in xrange(1, n+1) for t in ['x', 'o']) <= 1
    
    # columns
    for c in xrange(1, n+1):
        prob += lpSum(variables[(t,r,c)] for r in xrange(1, n+1) for t in ['x', 'o']) <= 1
    
    # diagonals r+c=k
    for k in xrange(2, 2*n+1):
        prob += lpSum(variables[(t,r,k-r)] for r in xrange(1, n+1) for t in ['+', 'o'] if 1 <= k-r <= n) <= 1
    
    # diagonals r-c=k
    for k in xrange(1-n, n):
        prob += lpSum(variables[(t,r,r-k)] for r in xrange(1, n+1) for t in ['+', 'o'] if 1 <= r-k <= n) <= 1
    
    # existing constraints
    for t, r, c in models:
        if t == 'o':
            prob += variables[t,r,c] == 1
        else:
            prob += variables[t,r,c] + variables['o',r,c] == 1
    
    prob.setObjective(lpSum(variables[(t,r,c)] * VALUE[t] for r in xrange(1, n+1) for c in xrange(1, n+1) for t in TYPES))
    
    # status = prob.solve(GLPK(msg = 0))
    status = prob.solve()
    assert LpStatus[status] == "Optimal"
    
    points = int(sum(value(v) * VALUE[t] for (t,r,c), v in variables.iteritems()))
    
    changed = []
    models = set(models)
    for (t,r,c), v in variables.iteritems():
        if value(v) > 0.5:
            if (t,r,c) not in models:
                changed.append((t,r,c))
    
    res = points, changed
    
    if verbose:
        sys.stderr.write(".")
        sys.stderr.flush()
    
    return res


def check(data):
    
    if verbose:
        sys.stderr.write(".")
        sys.stderr.flush()
    
    return res


if __name__ == '__main__':
    check_mode = False
    parallelize = False
    
    if len(sys.argv) > 1 and "-v" in sys.argv[1:]:
        verbose = True
    
    if len(sys.argv) > 1 and "-c" in sys.argv[1:]:
        check_mode = True
    
    if len(sys.argv) > 1 and "-p" in sys.argv[1:]:
        parallelize = True
        i = sys.argv.index("-p")
        if len(sys.argv) > i+1 and sys.argv[i+1].isdigit():
            processes = int(sys.argv[i+1])
        else:
            processes = 2
        
    t = int(sys.stdin.readline())
    if verbose:
        print >> sys.stderr, "Solving %d test cases" % t
    
    # read input
    test_cases = [read() for i in xrange(t)]
    
    # solve
    if parallelize:
        process_pool = Pool(processes=processes)
        if check_mode:
            test_results = process_pool.map_async(check, test_cases).get(9999999)
        else:
            test_results = process_pool.map_async(solve, test_cases).get(9999999)
    
    else:
        if check_mode:
            test_results = [check(data) for data in test_cases]
        else:
            test_results = [solve(data) for data in test_cases]
    
    if verbose:
        sys.stderr.write("\n")
        sys.stderr.flush()
    
    # write output
    for i, res in enumerate(test_results):
        print "Case #%d:" % (i+1),
        write(res)


