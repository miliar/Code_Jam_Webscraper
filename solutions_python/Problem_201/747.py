import sys
from collections import defaultdict

__author__ = 'David'


T = int(sys.stdin.readline())

for t in xrange(T):
    N, K = [int(x) for x in sys.stdin.readline().strip().split(' ')]

    buckets = defaultdict(int)
    buckets[N] = 1

    while K > 0:
        #print N, K, buckets

        size = sorted(buckets.keys(), reverse=True)[0]
        count = min(buckets[size], K)
        K -= count
        #print '  ', size, count

        del buckets[size]

        if size % 2 == 0:
            buckets[size / 2] += count
            buckets[size / 2 - 1] += count
            if K == 0:
                print "Case #%d: %d %d" % (t + 1, size / 2, size / 2 - 1)
        else:
            buckets[size / 2] += count * 2
            if K == 0:
                print "Case #%d: %d %d" % (t + 1, size / 2, size / 2)
