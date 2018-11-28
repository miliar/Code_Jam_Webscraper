# usage:  (python3 a.py < a.in) > a.out
import time, sys, inspect

lineno = lambda: inspect.currentframe().f_back.f_back.f_lineno
print = lambda *a, **k: __builtins__.print(str(lineno())+':', *a, file=sys.stderr, **k)

#---------------------------------------------

'''

'''

from hopcroftkarp import HopcroftKarp

def run(data):

    c1 = []
    c2 = []
    for t in data:
        if t[1] == 1:
            c1.append(t[0])
        else:
            c2.append(t[0])

    c1.sort()
    c2.sort()
    c1 += [float('inf')] * max(len(c2)-len(c1), 0)
    c2 += [float('inf')] * max(len(c1)-len(c2), 0)
    n = len(c1)

    # print(c1, c2)
    graph = dict()
    c1h = list()
    for i,c in enumerate(c1):
        graph[(1,i,c)] = {(2,j,d) for j,d in enumerate(c2) if c != d}
        c1h.append((1,i,c))

    mm = HopcroftKarp(graph).maximum_matching()
    # print(mm)
    # print(c1h)
    diff = [c[2] for c in c1h if c not in mm]

    cars = diff.count(1)
    prom = len(diff) - cars

    return str(n + cars) + ' ' + str(prom)





    # # grid = []
    # # for c in c1:
    # #     grid.append([(c,d) for d in c2])
    # cars = n
    # prom = 0

    # for it in range(n):

    #     print(grid)

    #     min_i = None
    #     min_i_val = float('inf')
    #     for i in range(n):
    #         lval = len([x for x in grid[i] if x[0] != x[1]])
    #         if lval < min_i_val:
    #             min_i_val = lval
    #             min_i = i

    #     min_j = None
    #     min_j_val = float('inf')
    #     for j in range(n):
    #         lval = len([grid[k][j] for k in range(n) if grid[k][j][0] != grid[k][j][1]])
    #         if lval < min_j_val:
    #             min_j_val = lval
    #             min_j = j

    #     print(min_i, min_j)
    #     if min_i < min_j:
    #         for j0 in range
    #         j0 = 0

#---------------------------------------------

def read_case():
    _, _, m = [int(k) for k in list(input().split())]
    return [[int(k) for k in list(input().split())] for i in range(m)]

for i in range(int(input())):
    outstr = 'Case #'+str(i+1)+': '+str(run(read_case()))
    print(outstr, ' @ t =', time.clock())
    __builtins__.print(outstr)
