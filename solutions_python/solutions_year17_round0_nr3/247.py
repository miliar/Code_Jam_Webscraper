from heapq import *

class Run(object):
    __slots__ = ['length', 'count']
    def __init__(self, length, count):
        self.length = length
        self.count = count

    def __hash__(self):
        return hash(self.length)

    def __eq__(self, other):
        return self.length == other.length

    def __lt__(self, other):
        # Backwards for heap
        return self.length > other.length

    def split(self):
        if self.length % 2 == 0:
            b = self.length / 2
            a = b - 1
        else:
            a = b = (self.length - 1) / 2
        return a, b
    

def lastStall(n, k):
    heap = []
    d = {}
    r = Run(n,1)
    heappush(heap, r)
    d[r.length] = r
    while k > 0:
        r = heappop(heap)
        a, b = r.split()
        if a not in d:
            d[a] = Run(a, 0)
            heappush(heap, d[a])
        if b not in d:
            d[b] = Run(b, 0)
            heappush(heap, d[b])
        d[a].count += r.count
        d[b].count += r.count
        k -= r.count
        del d[r.length]
    return b, a
            
if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t+1):
        n, k = map(int, raw_input().split())
        a, b = lastStall(n, k)
        print "Case #%d: %d %d" % (i, a, b)
