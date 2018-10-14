#!/usr/bin/python

cases = int(raw_input())

for case in range(1, cases + 1):
    # R = rides in a day
    # k = ride capacity
    # N = number of groups
    R, k, N = map(int, raw_input().split())
    groups = map(int, raw_input().split())
    rides = [None] * N
    # Run through simulation
    g = 0   # group index
    cost = 0
    for r in range(R):
        if rides[g] == None:
            # Compute entry for group g
            tempRide = []
            tempGroup = g
            while sum(tempRide) + groups[tempGroup] <= k:
                tempRide.append(groups[tempGroup])
                tempGroup = (tempGroup + 1) % N
                if tempGroup == g:
                    # Made it all the way around
                    break
            rides[g] = [(g + len(tempRide)) % N, sum(tempRide)]
        cost += rides[g][1]
        g = rides[g][0]
    print 'Case #%d: %d' % (case, cost)
