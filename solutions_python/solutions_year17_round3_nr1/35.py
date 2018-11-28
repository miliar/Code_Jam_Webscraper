import sys
import math

def best_area(pancakes, K):
    """pancakes: [ (r*h, r) ]"""
    sumK = sum(pan[0] for pan in pancakes[:K])
    maxRK = max(pan[1] for pan in pancakes[:K])
    best_using_K = maxRK**2 + 2*sumK
    best_area = best_using_K
    if len(pancakes) > K:
        sumKminus1 = 0 if K==1 else sum(pan[0] for pan in pancakes[:K-1])
        maxRKminus1 = 0 if K==1 else max(pan[1] for pan in pancakes[:K-1])
        for other in pancakes[K:]:
            curr_sum = sumKminus1 + other[0]
            curr_maxR = max(maxRKminus1, other[1])
            curr_area = curr_maxR**2 + 2*curr_sum
            if curr_area > best_area:
                best_area = curr_area
    return math.pi * best_area


if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        N, K = [int(part) for part in sys.stdin.readline().split()]
        assert 1 <= K <= N
        pancakes = []
        for _ in xrange(N):
            rad, ht = [int(part) for part in sys.stdin.readline().split()]
            pancakes.append((rad*ht, rad))
        pancakes.sort(reverse=True)
        best = best_area(pancakes, K)
        print "Case #%d: %.9f" % (i+1, best)
