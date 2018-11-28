import sys

def solve():
    a, b = sys.stdin.readline().split()
    smax = int(a)
    seq = []
    for i, x in enumerate(map(int, b)):
        for _ in xrange(x):
            seq.append(i)
    seq.sort()
    ans = 0
    for i, x in enumerate(seq):
        ans = max(ans, max(0, x - i))
    return ans

t = int(sys.stdin.readline())
for i in xrange(1, t+1):
    print 'Case #%d: %d' % (i, solve())