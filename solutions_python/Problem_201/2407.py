import heapq

class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __cmp__(self, other):
        if self.end - self.start > other.end - other.start:
            return -1
        elif self.end - self.start < other.end - other.start:
            return 1
        else:
            if self.start < other.start:
                return -1
            elif self.start > other.start:
                return 1
            else:
                return 0

T = int(raw_input())
for i in xrange(1, T+1):
    N, k = (int(x) for x in raw_input().split())
    intervals = []
    heapq.heappush(intervals, Interval(0, N-1))

    while k > 1:
        next_interval = heapq.heappop(intervals)
        start = next_interval.start
        end = next_interval.end
        midpoint = start + (end - start)/2
        if start <= midpoint-1:
            heapq.heappush(intervals, Interval(start, midpoint-1))
        if midpoint+1 <= end:
            heapq.heappush(intervals, Interval(midpoint+1, end))
        k -= 1
        
    next_interval = heapq.heappop(intervals)
    start = next_interval.start
    end = next_interval.end
    midpoint = start + (end - start)/2
    max_dist, min_dist = max(midpoint-start, end-midpoint), min(midpoint-start, end-midpoint)

    print "Case #{}: {} {}".format(i, max_dist, min_dist)
