# N by N square of cells to place models in
# +, x are worth 1
# o is worth 2
# if two models are in same row or column, one must be +
#   IOW every row/column may have at most one non-+ model
# if two models are in same diagonal, one must be x
#   IOW every diagonal may have at most one non-x model
# number of model placements are given up front
#
# N <= 100
# need to use dynamic programming somehow...
# possible to separate problem into selection of model/empty and then selection
# of what kind of model each one is?

# solution may place new models or upgrade + and x models to o models

# what's optimal unconstrained solution?
# N = 1: 2
# o
# N = 2: 5
# o+
# +x
# N = 3: 7
# o++
# .x.
# .+x
#
# 7
# +o+
# x..
# .+x

# recursive descent, have array with number of conflicts for each model type

# simple recursive descent might blow stack for N = 100, although maybe not if we don't spend stack frames on cells with no remaining choice
# there's got to be some more structure here...

# what if we find optimal solution for just + and x and then promote to o those cells that we can?

# view as max sat?

# problem can be separated!!! view o as + and x on the same square, then constraints are:
# every cell may have at most one x
# a row/col may have at most one x
# every cell may have at most one +
# a diagonal may have at most one +

# ok so given an inital set of x's, easy to find more x's so that every row and every column has an x: sort unoccupied rows and cols and fill in one by one
# given initial set of +'s, how to place more +'s so max diagonals have a +?
# make list of pairs of diagonals that have available spots, then max match??
# sure why not

# hopcroft-karp algorithm

from collections import defaultdict

def max_match(edges):
    """
    Return the largest disjoint subset of 'edges', which describes a set of
    edges linking two disjoint sets (a bipartite graph).
    """
    l_adj = defaultdict(list)
    r_adj = defaultdict(list)
    for l, r in edges:
        l_adj[l].append(r)
        r_adj[r].append(l)
    l_free = set(l for (l, r) in edges)
    r_free = set(r for (l, r) in edges)
    matches = set()
    while True:
        l_q = list(l_free)
        l_pred = {}
        r_pred = {}
        hit_r_free = False
        while l_q:
            r_q = []
            for l in l_q:
                for r in l_adj[l]:
                    if (l, r) in matches:
                        continue # forward edge must be untaken
                    if r in r_pred:
                        continue # dest may not already have been visited
                    r_pred[r] = l
                    r_q.append(r)
                    if r in r_free:
                        hit_r_free = True
            if hit_r_free:
                break
            l_q = []
            for r in r_q:
                for l in r_adj[r]:
                    if (l, r) not in matches:
                        continue # reverse edge must be taken
                    if l in l_pred:
                        continue # dest may not already have been visited
                    l_pred[l] = r
                    l_q.append(l)
        if not hit_r_free:
            break # we've found maximal matching
        assert r_q
        for r in r_q:
            if r not in r_free:
                continue
            l = r_pred[r]
            while l in l_pred:
                l = r_pred[l_pred[l]]
            if l not in l_free:
                continue
            # OK, we have alternating path between two free vertices, make the
            # change
            l_free.remove(l)
            r_free.remove(r)
            l = r_pred[r]
            matches.add((l, r))
            while l in l_pred:
                r = l_pred[l]
                matches.remove((l, r))
                l = r_pred[r]
                matches.add((l, r))
    return matches

def solve(n, models):
    # solve x_board
    open_r = set(range(n))
    open_c = set(range(n))
    x_sol = set()
    for kind, r, c in models:
        if kind not in 'xo':
            continue
        assert r in open_r
        assert c in open_c
        open_r.remove(r)
        open_c.remove(c)
        x_sol.add((r, c))
    x_sol_orig = x_sol.copy()
    for r, c in zip(sorted(open_r), sorted(open_c)):
        x_sol.add((r, c))

    # solve p_board
    open_plus = set(xrange(2 * n - 1))
    open_minus = set(xrange(-n + 1, n))
    p_sol = set()
    for kind, r, c, in models:
        if kind not in '+o':
            continue
        assert r + c in open_plus
        assert r - c in open_minus
        open_plus.remove(r + c)
        open_minus.remove(r - c)
        p_sol.add((r, c))
    p_sol_orig = p_sol.copy()
    edges = []
    for r in xrange(n):
        for c in xrange(n):
            if r + c in open_plus and r - c in open_minus:
                edges.append((r + c, r - c))
    matches = max_match(edges)
    for (plus, minus) in matches:
        r = (plus + minus) / 2
        c = (plus - minus) / 2
        p_sol.add((r, c))

    sol = []
    for r in xrange(n):
        for c in xrange(n):
            is_x = (r, c) in x_sol
            is_p = (r, c) in p_sol
            is_x_orig = (r, c) in x_sol_orig
            is_p_orig = (r, c) in p_sol_orig
            if is_x == is_x_orig and is_p == is_p_orig:
                continue
            if is_x and is_p:
                sol.append(('o', r, c))
            elif is_x:
                sol.append(('x', r, c))
            elif is_p:
                sol.append(('+', r, c))
    return len(x_sol) + len(p_sol), sol

if __name__ == '__main__':
    import sys
    fp = open(sys.argv[1])
    def readline():
        return fp.readline().strip()
    num_cases = int(readline())
    for i in xrange(num_cases):
        n, m = [int(x) for x in readline().split()]
        models = []
        for j in xrange(m):
            kind, r, c = readline().split()
            models.append((kind, int(r) - 1, int(c) - 1))
        score, sol = solve(n, models)
        print "Case #%d: %d %d" % (i + 1, score, len(sol))
        for (kind, r, c) in sol:
            print "%s %d %d" % (kind, r + 1, c + 1)
