import sys
from datetime import datetime
from math import acos

def debug(x):
    sys.stderr.write('{} DEBUG: {}\n'.format(datetime.now().time(), x))

PI = 2.0*acos(0.0)

def face(r):
    return PI*r*r

def dowr(r, h):
    return 2.*PI*r*h

def solve(N, K):
    pancakes = []
    for i in xrange(N):
        pancakes.append(tuple(map(int, raw_input().split())))
    pancakes = sorted(pancakes, reverse=True)
    best = [[0]*(K+2) for _ in xrange(N+2)]
    for i in xrange(N):
        for j in xrange(1, min(K, i+1)):
            pass

def solvesmall(N, K):
    pancakes = []
    for i in xrange(N):
        pancakes.append(tuple(map(int, raw_input().split())))
    pancakes = sorted(pancakes, reverse=True)
    best = 0.
    for i in xrange(1<<N):
        used = [pancakes[x] for x in xrange(N) if (1<<x & i)]
        if len(used)!=K:
            continue;
        prv = 0.
        cur = 0.
        for r,h in reversed(used):
            cur += dowr(r, h) + face(r) - prv
            prv = face(r)
        #debug((i,cur))
        best = max(best, cur)
    return best


def main():
    T = int(raw_input())
    for tc in xrange(1, T+1):
        debug("Running test #{}...\n".format(tc))
        N, K = map(int, raw_input().split())
        print "Case #{}: {:.8f}".format(tc, solvesmall(N, K))


if __name__ == "__main__":
    main()
