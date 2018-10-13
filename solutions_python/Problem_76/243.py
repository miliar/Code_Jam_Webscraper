import sys
import itertools

T = int(sys.stdin.readline())

for _t in xrange(T):

    N = int(sys.stdin.readline())
    candies = [int(x) for x in sys.stdin.readline().split()]



    if reduce(lambda x, y: x^y, candies) != 0:
        print "Case #%d:" % (_t+1), "NO"
        continue

    n = 0
    total = 0
    while n < N:
        total += candies[n]
        n += 1

    total -= min(candies)

    print "Case #%d:" % (_t+1), total

        
