from functools import *

inf = open('B-large.in')
ouf = open('B-large.out', 'w')
input = lambda: inf.readline().strip()
print = partial(print, file = ouf)


def solve():
    d = int(input())
    p = list(map(int, input().split()))
    print(min(m + sum(x // m + int(x % m > 0) - 1 for x in p) for m in range(1, max(p) + 1)))
    
    
tests = int(input())
for z in range(tests):
    print("Case #{}: ".format(z + 1), end = '')
    solve()

ouf.close()