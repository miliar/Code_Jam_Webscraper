# usage:  (py3 a.py < a.in) > a.out

import time, sys, inspect
from itertools import combinations

lineno = lambda: inspect.currentframe().f_back.f_back.f_lineno
print = lambda *a, **k: __builtins__.print(str(lineno())+':', *a, file=sys.stderr, **k)
map = lambda *a: list(__builtins__.map(*a))
reversed = lambda *a: list(__builtins__.reversed(*a))

#---------------------------------------------

'''
max one non-'+' per row and col
    ie  count('x') + count('o') <= 1  per row and col
    ie  count('+') + count('o') <= 1  per diag

we have a max of
    2n-2 '+'s  (tho actual bound is tighter)
      n  'x's
      n  'o's

simplify without 'o's mb?
    ie  count('x') <= 1  per row and col
    ie  count('+') <= 1  per diag
    try to do one '+' into every diag
    try to do one 'x' into every row/col
            8-queens-puzzle like

an algorithm
    1. guess model 'o' position -> O(n^2)
    2. run greedy 'x'- and '+'-fill algo on that
        O(n^2) ?
    O(n^4) seems a bit slow, even for this small n
    plus, algo only for small i think

    not convinced that 'greedy' thing works at all

i think i have found a different algo
    for a restricted version with 'x's and '+'s
    but the 'o's are causing problems..
    luckily only one 'o' can possibly be in the first row

FINAL ALGO
    treat diag and row/col problem independently
    solve both (greedily) and if there is overlap combine '+' and 'x' into 'o'

'''

def style(grid):
    return sum(sum((2 if e == 'o' else 1 if e == 'x' or e == '+' else 0) for e in row) for row in grid)

def run(data):
    m, n, grid = data
    # print(grid)

    x_added = []
    p_added = []

    j = int(any(grid[0][i] == 'x' or grid[0][i] == 'o' for i in range(n)))

    if n == 1:
        if grid[0][0] != 'x' and grid[0][0] != 'o':
            x_added.append((0, 0))
        if grid[0][0] != '+' and grid[0][0] != 'o':
            p_added.append((0, 0))
    else:
        for i in range(n):
            if grid[0][i] == '+' or grid[0][i] == 'o':
                if i != 0 and i != n-1:
                    p_added.append((n-1, n-1-i))
            else:
                p_added.append((i, 0))
                if i != 0 and i != n-1:
                    p_added.append((n-1-i, n-1))

            if grid[0][i] != 'x' and grid[0][i] != 'o':
                x_added.append((j, i))
                j += 1

    ret = ''
    for p in p_added:
        y, x = p
        if (y, x) in x_added:
            ret += 'o ' + str(y+1) + ' ' + str(x+1) + '\n'
        elif grid[y][x] == 'x':
            ret += 'o ' + str(y+1) + ' ' + str(x+1) + '\n'
        else:
            ret += '+ ' + str(y+1) + ' ' + str(x+1) + '\n'

    cnt = len(p_added)
    for ex in x_added:
        y, x = ex
        if (y, x) in p_added:
            pass  # already handled above!
        elif grid[y][x] == '+':
            ret += 'o ' + str(y+1) + ' ' + str(x+1) + '\n'
            cnt += 1
        else:
            ret += 'x ' + str(y+1) + ' ' + str(x+1) + '\n'
            cnt += 1

    print(p_added, x_added)
    ret = str(style(grid) + len(p_added) + len(x_added)) + ' ' + str(cnt) + '\n' + ret

    return ret[:-1]


#---------------------------------------------

def read_case():
    n, m = [int(k) for k in list(input().split())]
    grid = []
    for i in range(n):
        grid.append([''] * n)
    for i in range(m):
        m, y, x = list(input().split())
        y, x = int(y), int(x)
        grid[y-1][x-1] = m
    return (m, n, grid)

for i in range(int(input())):
    outstr = 'Case #'+str(i+1)+': '+str(run(read_case()))
    print(outstr, ' @ t =', time.clock())
    __builtins__.print(outstr)
