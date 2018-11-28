import sys

def getbest(k):
    k.sort(reverse=True)
    if k[0] == 1:
        return 1
    best = k[0]
    if k[0] == 9:
        best = min(best, 1 + getbest(k[1:] + [3, 6]), 1 + getbest(k[1:] + [4, 5]))
    else:
        best = min(best, 1 + getbest(k[1:] + [k[0] - k[0] / 2, k[0] / 2]))
    return best

def solve():
    sys.stdin.readline()
    k = map(int, sys.stdin.readline().split())
    return getbest(k)

t = int(sys.stdin.readline())
for i in xrange(1, t+1):
    print 'Case #%d: %d' % (i, solve())