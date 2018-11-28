
import sys

stdin = sys.stdin

def solve(t, ns):
    n = len(ns)
    clapping = int(ns[0])
    needed = 0
    for i in xrange(1, n):
        if clapping >= i:
            clapping += int(ns[i])
        else:
            missing = i - clapping
            needed += missing
            clapping += missing
            clapping += int(ns[i])
    print "Case #%d: %d" % (t, needed)

T = int(stdin.readline())

for t in xrange(1, T + 1):
    line = stdin.readline().split()
    Smax, ns = int(line[0]), line[1]
    solve(t, ns)
