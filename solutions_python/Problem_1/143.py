#!/usr/bin/env python

import copy

def solve(engines, queries):
    switches = 0
    w_engines = copy.copy(engines) 

    while len(queries) > 0:
        # step 1
        while len(w_engines) > 1:
            q = queries.pop(0)
            
            if q in w_engines:
                w_engines.remove(q)

            if len(queries) == 0:
                return switches
            
        # step 2
        while len(queries) > 0:
            if queries[0] in w_engines:
                switches = switches + 1
                w_engines = copy.copy(engines)
                w_engines.remove(queries[0])
                break
            else:    
                queries.pop(0)
    
    return switches

def solve_problem(fname):
    l = [line.strip() for line in open(fname).readlines()]

    n_problems = int(l.pop(0))

    n = 1
    while n_problems > 0:
        n_se = int(l.pop(0))
        se = []
        for i in xrange(0, n_se):
            se.append(l.pop(0))

        n_q = int(l.pop(0))
        q = []
        for i in xrange(0, n_q):
            q.append(l.pop(0))

        print 'Case #%d: %d' % (n, solve(se, q))
        n = n + 1
        n_problems = n_problems - 1

if __name__ == '__main__':
    solve_problem('input.txt')
