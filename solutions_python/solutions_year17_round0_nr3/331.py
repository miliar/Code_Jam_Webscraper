import heapq
from collections import Counter

for case in xrange(1, int(raw_input()) + 1):
    print 'Case #{}:'.format(case),

    n, k = map(int, raw_input().split())
    queue = [-n]
    counter = Counter()
    counter[n] += 1

    i = 0
    while i < k:
        #print i, queue
        node = -heapq.heappop(queue)
        # print i, node, counter, queue

        s = (node-1) / 2
        l = (node-1) - s

        if not counter[s]: heapq.heappush(queue, -s)
        if not counter[l]: heapq.heappush(queue, -l)

        counter[s] += counter[node]
        counter[l] += counter[node]
        i += counter[node]

        del counter[node]

    print l, s
