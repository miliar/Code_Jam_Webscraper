from __future__ import with_statement
import sys
#import datetime

def qh(lst, limit):
    current = 0
    for i in xrange(limit):
        yield current
        current = lst[current]

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for c in xrange(1, T+1):
        R, k, N = map(int, f.readline().split())
        g = map(int, f.readline().split())
        assert len(g) == N

        S = sum(g)
        if S <= k:
            total = S * R
        else:
            #time1 = datetime.datetime.now()
            tmp = g+g
            queues, heads = [], []
            for i in xrange(N):
                size = 0
                for j in xrange(N):
                    if size + tmp[i+j] > k:
                        j -= 1
                        break
                    size += tmp[i+j]
                queues.append(size)
                heads.append((i+j+1)%N)

            #time2 = datetime.datetime.now()
            total = sum(queues[h] for h in qh(heads, R))
            #time3 = datetime.datetime.now()
            #print time2-time1, time3-time2

        print "Case #%d: %d" % (c, total)
