import sys
import heapq

from math import log

log2 = lambda x: log(x) / log(2)

def spaces(gapsize):
    space_both = (gapsize - 1)

    if space_both % 2 == 0:
        return space_both / 2, space_both / 2
    else:
        return space_both / 2 + 1, space_both / 2


def solve_slow(N, K):
    if N == K:
        return 0,0

    intervals = []

    def add_interval(a, b):
        size = b - a
        item = (-size, a)
        heapq.heappush(intervals, item)

    add_interval(0, N-1)

    k = K

    # print 'Solving stalls:', N, 'and persons:', K

    while k > 0:
        # print 'Person #%s' % (K-k+1)

        negsize, a = heapq.heappop(intervals)
        gapsize = -negsize + 1

        # print 'Got widest interval:', gapsize, a

        right, left = spaces(gapsize)

        # print '  has space (left, right):', left, right

        add_interval(a, a + left-1)
        add_interval(a + left + 1, a + left + right)

        k -= 1

    return spaces(gapsize)

def solve_fast(N, K):

    # If N was K, then K-dude would have to choose to go into a 1-length stall gap.
    # The dude's level would be floor(log2(K) + 1).
    # The dude's order within their level would be K - 2**(level-1).
    # When N is larger than K, by difference D, the dude would get a larger stall gap, by
    # additional size (N - K) / (2**(level-1)) - (1 if (K % (2**(level-1)) >= (N-K) % (2**(level-1)) )  else 0)

    level = int(log2(K)) + 1

    gap = 1

    gap += (N - K) / (2**(level-1))
    # if (K % (2**(level-1)) < (N-K) % (2**(level-1)) ):
    #     gap -= 1

    return spaces(gap)


def solve(N, K):
    ans = solve_fast(N, K)

    # ans2 = solve_slow(N, K)

    # if ans != ans2:
    #     print 'For N = %s, K = %s, got:' % (N, K)
    #     print '  Slow (correct) : %s %s' % ans2
    #     print '  Fast (wrong)   : %s %s' % ans
    #     sys.exit(1)

    return ans


def main():
    T = int(sys.stdin.readline().strip())

    for i in xrange(T):
        N, K = map(int, sys.stdin.readline().split())
        maxd, mind = solve(N, K)
        print 'Case #%s: %s %s' % (i+1, maxd, mind)

if __name__ == '__main__':
    main()
