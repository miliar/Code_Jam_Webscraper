#!/usr/bin/env python

import sys

line = lambda: map(int, sys.stdin.readline().split())

for t in range(1, line()[0] + 1):

    # Read input
    R, K, N = line()
    G = line()

    # Current state is a triple of #rides taken, queue position, and money made
    pos = rides = money = 0
    prev = [ None for _ in G ]  # store previous (rides, money) per position

    # This loop takes O(N) time because after N rides we are guaranteed to be
    # on a cycle, and then we will hit a break-out point within N rides. Since
    # boarding passengers inside the loop takes O(N) time too, the total running
    # time is O(N*N) per case.
    while rides < R:

        if prev[pos] is not None:
            # If we arrived here before, check if we can cut the cycle short:
            prev_rides, prev_money = prev[pos]
            if (R - rides)%(rides - prev_rides) == 0:
                money += (money - prev_money)*((R - rides)/(rides - prev_rides))
                break

        prev[pos] = (rides, money)

        # Board new passengers (up to N groups, and up to K total passengers):
        n = p = 0
        while n < N and p + G[pos] <= K:
            p += G[pos]
            n += 1
            pos = (pos + 1)%N
        rides += 1
        money += p

    # Print output
    print('Case #' + str(t) + ': ' + str(money))
