import sys
rl = lambda: sys.stdin.readline().strip()

t = int(rl())
for cc in range(t):
    r, k, n = map(int, rl().split())
    g = map(int, rl().split())

    lastSeen = [-1] * n
    rodeSoFar = [-1] * n

    beginWith = 0
    rides = r
    moneyEarned = 0
    while rides > 0:
        if lastSeen[beginWith] != -1:
            cycleLength = lastSeen[beginWith] - rides
            if rides >= cycleLength:
                cycleSize = moneyEarned - rodeSoFar[beginWith]
                cycles = rides / cycleLength
                """
                print "Cycle found: beginwith %d seen before" % beginWith
                print "cycleLength %d rides, cycle size %d" % (cycleLength,
                                                               cycleSize)
                print "%d rides remaining => %d cycles" % (rides, cycles)
                """
                moneyEarned += cycleSize * cycles
                rides -= cycleLength * cycles
                continue
        else:
            lastSeen[beginWith] = rides
            rodeSoFar[beginWith] = moneyEarned
        rideThisTime = 0
        rideUpto = beginWith-1
        groups = 0
        while groups < n and rideThisTime + g[(rideUpto+1) % n] <= k:
            rideUpto = (rideUpto+1) % n
            rideThisTime += g[rideUpto]
            groups += 1
        moneyEarned += rideThisTime
        """
        print ("starting from %d, %d people ride, next begin %d"
               % (beginWith, rideThisTime, (rideUpto+1)%n))
               """
        beginWith = (rideUpto+1) % n
        rides -= 1

    print "Case #%d: %d" % (cc+1, moneyEarned)


