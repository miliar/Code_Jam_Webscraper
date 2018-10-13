from functools import *
from collections import defaultdict as dd

inf = open('A-large.in')
ouf = open('A-large.out', 'w')
input = lambda: inf.readline().strip()
print = partial(print, file = ouf)


def solve():
    allowed = dd(lambda: set('><^v'))
    
    r, c = map(int, input().split())
    d = []
    for i in range(r):
        d.append(input().strip())
    for i in range(r):
        ars = [j for j in range(c) if d[i][j] != '.']
        if not ars:
            continue
        left, right = min(ars), max(ars)
        allowed[i, left] -= {'<'}
        allowed[i, right] -= {'>'}
    for j in range(c):
        ars = [i for i in range(r) if d[i][j] != '.']
        if not ars:
            continue
        top, bottom = min(ars), max(ars)
        allowed[top, j] -= {'^'}
        allowed[bottom, j] -= {'v'}
    result = 0
    for (i, j), allow in allowed.items():
        if allow:
            result += (d[i][j] not in allow)
        else:
            result = 'IMPOSSIBLE'
            break
    print(result)
    
    
tests = int(input())
for z in range(tests):
    print("Case #{}: ".format(z + 1), end = '')
    solve()

ouf.close()