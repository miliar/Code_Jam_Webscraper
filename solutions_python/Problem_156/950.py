import math
import heapq


def find_minimum(pancakes):
    minimum = 1000
    heap = [(-p, p, 1) for p in pancakes]
    heapq.heapify(heap)

    for i in xrange(max(pancakes)):
        if not pancakes:
            break
        top =  heapq.heappop(heap)
        #print top, i
        v, pancake, divisor = top
        minimum = min(minimum, (-v) + i)
        #print minimum
        divisor += 1
        heapq.heappush(heap,
                ((pancake / (divisor) + pancake % divisor)*-1,
                 pancake,
                 divisor))
    return minimum

for t in xrange(int(raw_input())):
    D = int(raw_input())
    pancakes = map(int, raw_input().split())
    value = find_minimum(pancakes)
    print 'Case #%d: %d' % (t+1, value)
