import heapq  # @UnresolvedImport
from sys import stdin

def main():
    t = int(stdin.readline().strip())
    for kk in xrange(1, t+1):
        n, k = (int(s) for s in stdin.readline().strip().split())
        
        heap = []
        heapq.heappush(heap, (-((n-1)/2), -(n/2), -0))
        for _ in xrange(k):
            left, right, offset = heapq.heappop(heap)
            left, right, offset = -left, -right, -offset
            #print "pop {} {} {}".format(left, right, offset)
            if left:
                #print "push {} {} {}".format((left-1)/2, left/2, offset)
                heapq.heappush(heap, (-((left-1)/2), -(left/2), -offset))
            if right:
                #print "push {} {} {}".format((right-1)/2, right/2, offset + left)
                heapq.heappush(heap, (-((right-1)/2), -(right/2), -(offset + left)))
            
        print "Case #{}: {} {}".format(kk, right, left)

main()
