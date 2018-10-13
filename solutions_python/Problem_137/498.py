from __future__ import print_function

import sys
import numpy as np

readline = sys.stdin.readline

def assert_equal(a, b):
    assert a == b, "%s != %s" % (a, b)

def solve_grid(g, m):
    r, c = g.shape
    if r > c:
        # transpose to ensure r < c
        g = g.T
        r, c = c, r
    
    if m == 0:
        assert_equal(g.sum(), m)
        return True
    
    elif r * c == m:
        g[:] = 1
        assert_equal(g.sum(), m)
        return True
    elif r * c == m+1:
        g[:] = 1
        g[-1,-1] = 0
        assert_equal(g.sum(), m)
        return True
    
    if r == 2:
        if m % 2 or (1 + m/2) == c:
            return False
        
        g[:,:m/2] = 1
        assert_equal(g.sum(), m)
        return True
    
    if m < c:
        if (c - m) > 1:
            g[0,:m] = 1
            assert_equal(g.sum(), m)
            return True
    else:
        # bite c and recurse
        if solve_grid(g[1:,:], m-c):
            g[0,:] = 1
            assert_equal(g.sum(), m)
            return True
    
    if m < r:
        if (r-m) > 1:
            g[:m,0] = 1
            assert_equal(g.sum(), m)
            return True
    else:
        # bite r and recurse
        if solve_grid(g[:,1:], m-r):
            g[:,0] = 1
            assert_equal(g.sum(), m)
            return True
    
    if m <= (r + c - 1 - 4):
        # check perimiter
        mc = min(c-2, m)
        assert_equal(len(g[0]), c)
        g[0,:mc] = 1
        mr = min(r-2, m-mc)
        g[1:1+mr, 0] = 1
        assert_equal(len(g[:,0]), r)
        assert_equal(g.sum(), m)
        return True
    
    
    return False

def show_grid(g):
    for i,row in enumerate(g):
        if i + 1 == g.shape[0]:
            row = row[:-1]
            end='c\n'
        else:
            end='\n'
        print(''.join(['*' if m else '.' for m in row]), end=end)

def _in(g, i, j):
    if i >= 0 and j >= 0 and i < g.shape[0] and j < g.shape[1]:
        return True
    return False

def nmines(g, i, j):
    n = 0
    if g[i,j]:
        return np.inf
    for x,y in neighbors(g, i, j):
        n += g[x,y]
    return n

def neighbors(g, i, j):
    points = []
    for x in (i-1,i,i+1):
        for y in (j-1,j,j+1):
            if x == i and y == j or not _in(g, x, y):
                continue
            points.append((x,y))
    return points

def verify(g, m):
    assert_equal(g.sum(), m)
    g2 = -1 * np.ones_like(g).astype('float')
    levelset = {(g.shape[0]-1, g.shape[1]-1)}
    while levelset:
        nextset = set()
        for i,j in levelset:
            n = g2[i,j] = nmines(g, i, j)
            if n == 0:
                for p in neighbors(g, i, j):
                    if g2[p] == -1:
                        nextset.add(p)
        levelset = nextset
    test = np.zeros_like(g)
    test[g2<0] = 1
    test[g2>=0] = 0
    assert (g == test).all(), "%s" % (g2)
    # assert (g == test).all(), "\n%s\n!=\n%s" % (g, test)

def outer_solve_grid(r, c, m):
    g = np.zeros((r,c), dtype=int)
    if r == 1:
        g[:,:m] = 1
        s = 1
    elif c == 1:
        g[:m,:] = 1
        s = 1
    else:
        s = solve_grid(g, m)
    if s:
        verify(g, m)
        show_grid(g)
    else:
        print("Impossible")
    return g


def test_case():
    R, C, M = [ int(s) for s in readline().split() ]
    # print(R, C, M)
    outer_solve_grid(R, C, M)

def main():
    T = int(readline())
    for i in range(1,T+1):
        print("Case #%i:" % i)
        test_case()

from IPython import get_ipython

if __name__ == '__main__' and not get_ipython():
    main()

