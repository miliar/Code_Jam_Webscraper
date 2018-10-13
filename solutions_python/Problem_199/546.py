"""
Flip from left to right, correcting each leftmost messed up pancake at
a time. If we reach the end and cannot finish: IMPOSSIBLE.

Proof?
"""

import sys

# HACK: Stack size large
# sys.setrecursionlimit(100000)

flip = {
    '-': '+',
    '+': '-'
}

"""
ps: String of '+' and '-' chars
K: flipper size
"""
def solve(ps, K):
    ps = list(ps)
    flips = 0
    for i,c in enumerate(ps):
        if c == '-':
            if len(ps)-i < K: # Check this
                return "IMPOSSIBLE"
            for j in xrange(i, i+K):
                ps[j] = flip[ps[j]]
            flips += 1
    return str(flips)

memo = {}
doing = set()
"""
Brute force + dp solve
"""
def solve2(ps, K):
    print ps
    if ps in memo: return memo[ps]
    if ps in doing: return None
    doing.add(ps)
    minflips = None
    for i in xrange(len(ps)-K+1):
        flipped = list(ps)
        for j in xrange(i, i+K):
            flipped[j] = flip[flipped[j]]
        cost = solve2("".join(flipped), K)
        if cost is None: continue
        if minflips is None or cost < minflips:
            minflips = cost + 1
    memo[ps] = minflips
    return minflips

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        ps, K = sys.stdin.readline().strip().split()
        K = int(K)
        # global memo
        # memo = {}
        # memo['+'*len(ps)] = 0
        print "Case #%d: %s" % (i+1, solve(ps, K))
        # print "Case #%d: %s" % (i+1, solve2(ps, K))
