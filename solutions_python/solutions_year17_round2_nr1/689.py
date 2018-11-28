from itertools import \
    product, \
    permutations, \
    combinations, \
    combinations_with_replacement
from functools import reduce, lru_cache
from math import floor,ceil,inf,sqrt

def intercept_time(i,j):
    if i[1] == j[1]:
        return inf
    else:
        return (j[0]-i[0])/(i[1]-j[1])

def intercept_distance(i,j):
    if intercept_time(i,j) < 0:
        return inf
    else:
        return intercept_time(i,j)*i[1] + i[0]

def solve(D, horses):
    horses.sort()
    while len(horses) > 1:
        if intercept_distance(horses[-2], horses[-1]) < D:
            del horses[-2]
        else:
            del horses[-1]
    return D / intercept_time(horses[0], (D,0))

if __name__ == '__main__':
    import sys,re
    data = iter(sys.stdin.read().splitlines())
    T = int(next(data))
    for (case_num, case) in enumerate(data):
        D,N = map(int, case.split())
        horses = []
        for _ in range(N):
            horses.append(tuple(map(int, next(data).split())))
        print('Case #{}: {}'.format(case_num+1, solve(D, horses)))
