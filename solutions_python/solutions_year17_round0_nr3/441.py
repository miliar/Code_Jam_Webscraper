# sol1: using heap to determine the best interval so far
import heapq
def sol1(n, k):
    stalls = [-n]
    heapq.heapify(stalls)
    rmax, rmin = 0, 0
    for _ in xrange(k):
        best = -heapq.heappop(stalls)
        if best % 2 == 0:
            rmax, rmin = best / 2, best /2 -1
        else:
            rmax, rmin = (best - 1) /2, (best - 1)/2

        if rmax:
            heapq.heappush(stalls, -rmax)
        if rmin:
            heapq.heappush(stalls, -rmin)
    return rmax, rmin
# sol2: since only two consecutive numbers are possible
# so no need to keep a heap
def sol2(n, k):
    u, v = 1, 0
    while k - u - v > 0:
        k -= u + v
        if n % 2 == 0:
            u, v = u, u + 2*v
        else:
            u, v = 2*u + v, v
        n /= 2

    if n % 2 == 0:
        if k - u <= 0:
            return n/2, max(n/2-1,0)
        else:
            return (n-1)/2, (n-1)/2
    else:
        if k-u <=0:
            return n/2, n/2
        else:
            return (n-1)/2 ,max((n-1)/2-1,0)
        



    
if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t+1):
        n, k = map(int, raw_input().split(' '))
        rmax, rmin = sol2(n, k)
        print "Case #{}: {} {}".format(i, rmax, rmin)
