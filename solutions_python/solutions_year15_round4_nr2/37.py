from functools import *
from fractions import Fraction

inf = open('B-small-attempt0.in')
ouf = open('B-small-attempt0.out', 'w')
input = lambda: inf.readline().strip()
print = partial(print, file = ouf)

foo = 'IMPOSSIBLE'


def solve():
    n, v, x = input().split()
    n = int(n)
    v = Fraction(v)
    x = Fraction(x)
    r, c = [0] * n, [0] * n
    for i in range(n):
        r[i], c[i] = map(Fraction, input().split())
    
    if n == 1:
        if c[0] == x:
            print(float(v / r[0]))
        else:
            print(foo)
        return
    
    if n == 2:
        if c[0] == c[1]:
            if c[0] == x:
                print(float(v / (r[0] + r[1])))
            else:
                print(foo)
            return
        t0 = v * (x - c[1]) / (r[0] * (c[0] - c[1]))
        t1 = (v - r[0] * t0) / r[1]
        if t0 >= 0 and t1 >= 0 and r[0] * t0 + r[1] * t1 == v and r[0] * t0 * c[0] + r[1] * t1 * c[1] == v * x:
            print(float(max(t0, t1)))
        else:
            print(foo)
        return
    
    print('Unimplemented')
    
    
    
tests = int(input())
for z in range(tests):
    print("Case #{}: ".format(z + 1), end = '')
    solve()

ouf.close()