#!/usr/bin/env python
from __future__ import unicode_literals
import decimal
import fractions
import sys


def compute_result(N, Q, horses, distLookup, deliveries):
    # make a dp array of the minimum time from each city, assuming we
    # were to switch horses, to the destination, starting from the
    # back and working backwards
    i = N-2
    dp = [-1]*N
    dp[N-1] = 0
    while i >= 0:
        distance, speed = horses[i]
        best_time = -1
        dist_to_city_j = 0
        for j in xrange(i+1, N):
            if dp[j] == -1:
                continue
            # how long does it take to get to city j from i, using j's
            # horse
            # try traveling there
            dist_j1_j = distLookup[(j-1, j)]
            assert dist_j1_j >= 0
            dist_to_city_j += dist_j1_j
            if distance < dist_to_city_j:
                break
            travel_time_to_city_j = fractions.Fraction(dist_to_city_j, speed)
            if best_time == -1 or best_time > travel_time_to_city_j + dp[j]:
                best_time = travel_time_to_city_j + dp[j]
        dp[i] = best_time
        i -= 1
    return decimal.Decimal(dp[0].numerator) / decimal.Decimal(dp[0].denominator)


def main(argv=sys.argv):
    infile = argv[1]
    outfile = argv[2]
    with open(infile) as f, open(outfile, 'w') as g:
        T = int(f.readline().strip())
        
        for case in xrange(1, T+1):
            N, Q = map(int, f.readline().strip().split())
            horses = []
            for _ in xrange(N):
                distance, speed = map(int, f.readline().strip().split())
                horses.append([distance, speed])
            distLookup = {}
            for i in xrange(N):
                distances = map(int, f.readline().strip().split())
                for j, d in enumerate(distances):
                    if d != -1:
                        distLookup[(i, j)] = d
            deliveries = []
            for _ in xrange(Q):
                U, V = map(int, f.readline().strip().split())
                deliveries.append((U, V))
            
            result = compute_result(N, Q, horses, distLookup, deliveries)
            g.write("Case #{}: {}\n".format(case, result))
    return 0

if __name__ == "__main__":
    status = main(argv=sys.argv)
    sys.exit(status)
