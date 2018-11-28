import collections
from fractions import gcd

def solve():
    N, P = map(int, raw_input().split())
    R = map(int, raw_input().split())
    packages = [list() for a in xrange(N)]
    for i in xrange(N):
        packages[i] = map(int, raw_input().split())
        packages[i].sort()

    res = 0
    while all(len(a) != 0 for a in packages):
        serves = min(int(packages[a][-1]/(R[a]*0.9)) for a in xrange(N))

        if not all((R[a]*serves)*1.1 >= packages[a][-1] for a in xrange(N)):
            big_index = 0
            big = 0
            for n in xrange(N):
                if packages[n][-1] > big:
                    big = packages[n][-1]
                    big_index = n
            packages[big_index].pop(-1)
            continue

        for n in xrange(N):
            packages[n].pop(-1)

        res += 1

    return res

T = int(raw_input())
for tt in xrange(T):
    print 'Case #{}: {}'.format(tt+1, solve())
