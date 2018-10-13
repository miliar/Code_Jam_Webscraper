import math
import heapq


def topsize(r, h):
    return math.pi * r * r


def ringsize(r, h):
    return 2 * math.pi * r * h


def maximize(pancakes, k, minimum):
    pq = []
    rt, ht = pancakes[minimum]
    total = topsize(rt, ht) + ringsize(rt, ht)
    # print "Total for {}: {}".format(minimum, total)
    for t in xrange(minimum + 1, len(pancakes)):
        r, h = pancakes[t]
        ring = ringsize(r, h)
        heapq.heappush(pq, ring)
        total += ring
        if len(pq) > k - 1:
            rem = heapq.heappop(pq)
            total -= rem
    return total


cases = int(raw_input())

for ctr in xrange(cases):
    ss = raw_input().split(" ")
    n = int(ss[0])
    k = int(ss[1])
    pancakes = []
    for z in xrange(n):
        ss = raw_input().split(" ")
        r = float(ss[0])
        h = float(ss[1])
        pancakes.append((r, h))

    pancakes.sort()
    pancakes.reverse()

    answer = 0.0
    for i in xrange(n):
        temp = maximize(pancakes, k, i)
        if temp > answer:
            answer = temp

    print "Case #{}: {:.12f}".format(ctr + 1, answer)
