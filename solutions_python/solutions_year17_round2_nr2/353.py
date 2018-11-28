import sys
from collections import Counter
read = lambda f=int: map(f, sys.stdin.readline().split())
T, = read()
def solve(cnt):
    (c1, d1), (c2, d2), (c3, d3) = cnt.most_common()
    if d1 > d2+d3:
        return 'IMPOSSIBLE'
    return (c1+c2+c3)*(d2+d3-d1) \
            + (c1+c2)*(d1-d3) \
            + (c1+c3)*(d1-d2)

for case in range(T):
    N, R, O, Y, G, B, V = read()
    cnt = Counter({'R':R,'Y':Y,'B':B})
    res = solve(cnt)
    print('Case #{}: {}'.format(case+1, res))

