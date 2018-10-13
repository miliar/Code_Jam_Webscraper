from collections import defaultdict
import sys
from heapq import *

filename = sys.argv[1]

f = open('%s.in' % filename)
g = open('%s.out' % filename, 'w')

DEBUG = sys.argv[2] if len(sys.argv) >= 3 else False
def dlog(s, *n):
    if DEBUG:
        if n:
            print(s % tuple(n))
        else:
            print(s)

T = int(f.readline())
for t in range(T):
    dlog("Case %d", t)
    line = f.readline().strip().split()
    n = int(line[0])
    k = int(line[1])

    spots = {n: 1}
    while True:
        dlog("spots %r, n %d", spots, k)
        level = sum(spots.itervalues())
        if level >= k:
            if len(spots) == 1:
                val = spots.popitem()[0] - 1
            else:
                vals = sorted(list(spots.iterkeys()), reverse=True)
                if k <= spots[vals[0]]:
                    val = vals[0] - 1
                else:
                    val = vals[1] - 1
            ans = (val - val/2, val/2)
            break

        next_spots = defaultdict(int)
        for gap, num in spots.iteritems():
            gap -= 1
            next_spots[gap - gap/2] += num
            next_spots[gap/2] += num
        spots = next_spots
        k -= level

    g.write('Case #%d: %d %d' % (t + 1, ans[0], ans[1]))
    g.write('\n')


