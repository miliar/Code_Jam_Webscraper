from math import log
from fractions import gcd

memo = {}

def partElf(P, Q):
    g = gcd(P, Q)
    P /= g
    Q /= g

    if (P,Q) in memo:
        return memo[(P,Q)]
    if P == Q:
        return 0
    if P > Q:
        return 41
    if int(log(Q, 2)) != log(Q, 2):
        return 41
    if P == 1:
        return int(log(Q, 2))
    
    minGen = 41

    for i in range(1, P):
        minGen = min(minGen, 1+partElf(i, Q / 2))

    memo[(P,Q)] = minGen
    return minGen


from sys import stdin

input = stdin.read().split('\n')

for t in range(int(input[0])):
    P, Q = map(int, input[t+1].split('/'))
    
    ans = partElf(P, Q)

    print "Case #{0}: {1}".format(t+1, "impossible" if ans > 40 else ans)