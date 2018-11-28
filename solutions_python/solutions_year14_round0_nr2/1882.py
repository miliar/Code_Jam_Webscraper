from functools import *
from decimal import *
from fractions import Fraction

inf = open('B-large.in')
ouf = open('output.txt', 'w')
input = lambda: inf.readline().strip()
print = partial(print, file = ouf)


def div_up(a, b):
    return a // b + int(a % b != 0)


def solve():
    c, f, x = map(lambda s: int(Decimal(s) * 10 ** 5), input().split())
    if x <= c:
        print(x / 2 / 10 ** 5)
        return
    farms = max(0, div_up(x * f - 2 * 10 ** 5 * c, c * f) - 1)
    print(sum(c / (2 * 10 ** 5 + i * f) for i in reversed(range(farms))) + x / (2 * 10 ** 5 + farms * f))
    
    
    
tests = int(input())
for z in range(tests):
    print("Case #{}: ".format(z + 1), end = '')
    solve()

ouf.close()