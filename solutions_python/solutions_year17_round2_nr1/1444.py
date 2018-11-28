import sys
from collections import namedtuple

Horse = namedtuple('Horse', ['k', 's'])

def solve(d, horses):
    max_time = 0
    for h in horses:
        max_time = max(max_time, (1.0/h.s)*(d - h.k))
    return d / max_time

t = int(sys.stdin.readline())
for i in xrange(1, t + 1):
    d, n = (int(i) for i in sys.stdin.readline().split())
    horses = []
    for _ in xrange(n):
        k, s = (int(i) for i in sys.stdin.readline().split())
        horses.append(Horse(k=k, s=s))
    max_speed = solve(d, horses)
    print 'Case #{}: {}'.format(i, max_speed)