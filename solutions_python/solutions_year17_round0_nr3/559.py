"""
Using the tree method. Solve?
"""

import sys

def split(n):
    if n % 2 == 1:
        return ((n-1)/2, (n-1)/2)
    else:
        return (n/2, n/2 - 1)

def solve(N, K):
    steps = []
    vals = {N: 1}
    while len(vals) > 0:
        newvals = {}
        ks = sorted(vals.keys(), reverse=True)
        for k in ks:
            s = split(k)
            if s[0] != 0:
                if s[0] not in newvals:
                    newvals[s[0]] = vals[k]
                else:
                    newvals[s[0]] += vals[k]
            if s[1] != 0:
                if s[1] not in newvals:
                    newvals[s[1]] = vals[k]
                else:
                    newvals[s[1]] += vals[k]
            steps.append((s, vals[k]))
        vals = newvals
    ind = 0
    for s,c in steps:
        ind += c
        if ind >= K: return s
    assert False

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        N,K = map(int, sys.stdin.readline().strip().split())
        a,b = solve(N,K)
        print "Case #%d: %d %d" % (i+1, a, b)
