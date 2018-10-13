"""https://code.google.com/codejam/contest/dashboard?c=3264486#s=p2"""

from math import ceil, floor, log2

def solve(n, k):
    level = int(log2(k))
    space = ceil( (n - (k - 1)) / 2**level )
    split = (space - 1) / 2
    return ceil(split), floor(split)

if __name__ == '__main__':
    for i in range(int(input())):
        n, k = map(int, input().split())
        res = solve(n, k)
        print('Case #{}: {} {}'.format(i + 1, res[0], res[1]))
