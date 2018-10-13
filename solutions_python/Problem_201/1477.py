from Queue import PriorityQueue
from sys import stderr
import math
def floor(a):
    return int(math.floor(a)+0.00001)
def ceil(a):
    return int(math.ceil(a)+0.00001)

T = input()
lines = {test: tuple(map(int, raw_input().split())) for test in xrange(T)}
seen = {}
results = {lines[x] for x in lines}

class Interval():
    def __init__(self, (d1, d2)):
        self.i = min([d1, d2])
        self.a = max([d1, d2])
    def __cmp__(self, oth):
        if self.i == oth.i and self.a == oth.a:
            return 0
        elif self.i > oth.i:
            return -1
        elif self.i == oth.i and self.a > oth.a:
            return -1
        else:
            return 1
    def __repr__(self):
        return "Interval((%d, %d))" % (self.i, self.a)
def occ(x):
    return ceil(x/2.)-1, floor(x/2.)

for N, K in sorted(lines.itervalues(), key=lambda a: (-a[0], -a[1])):
    #N, K = map(int, raw_input().split())
    if (N, K) in seen:
        end = seen[(N, K)]
    else:
        pq = PriorityQueue()
        pq.put(Interval(occ(N)))
        for person in xrange(K):
            s = pq.get()
            #print s
            a = Interval(occ(s.i))
            b = Interval(occ(s.a))
            pq.put(a)
            pq.put(b)
            end = s
            if (N, person+1) in results:
                seen[(N, person+1)] = s
for test in xrange(T):
    end = seen[lines[test]]
    print "Case #%d: %d %d" % (test+1, end.a, end.i)
