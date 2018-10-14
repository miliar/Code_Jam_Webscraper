from functools import *

inf = open('A-large.in')
ouf = open('A-large.out', 'w')
input = lambda: inf.readline().strip()
print = partial(print, file = ouf)


def solve():
    n, nums = input().strip().split()
    n = int(n)
    result = 0
    count = 0
    for i, x in enumerate(map(int, nums)):
        if x > 0:
            if count < i:
                result += i - count
                count = i
            count += x
    print(result)
    
    
    
tests = int(input())
for z in range(tests):
    print("Case #{}: ".format(z + 1), end = '')
    solve()

ouf.close()