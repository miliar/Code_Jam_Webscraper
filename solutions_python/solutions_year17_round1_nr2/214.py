from math import ceil, floor
from itertools import permutations
def solve1(p, r, q):
    c = 0
    for x in q:
        if int(x/(0.9*r)) >= x/(1.1*r):
            c += 1
    return c

def solve2(p, r, q):
    q[0] = sorted(q[0])
    q[1] = sorted(q[1])
    c = []
    for perm in permutations(q[1]):
        c.append(0)
        for a, b in zip(q[0], perm):
            a_l = int(ceil(a/(1.1*r[0])))
            a_r = int(a/(0.9*r[0]))
            b_l = int(ceil(b/(1.1*r[1])))
            b_r = int(b/(0.9*r[1]))
            if a_l > a_r: continue
            if b_l > b_r: continue
            if (b_r < a_l) or (a_r < b_l): continue
            c[-1] += 1
    return max(c)

def solve(n, p, r, q):
    if n == 1:
        return solve1(p, r[0], q[0])
    else:
        return solve2(p, r, q)

for case in range(1, int(input())+1):
    n, p = map(int, input().split())
    r = list(map(int, input().split()))
    q = []
    for i in range(n):
        q.append(list(map(int, input().split())))
    print('Case #{}: {}'.format(case, solve(n, p, r, q)))
