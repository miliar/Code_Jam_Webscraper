numCases = int(input())
for i in range(1, numCases+1):
    distance, numHorses = [int(s) for s in raw_input().split(" ")]

    maxHrs = 0
    for h in xrange(numHorses):
        currentDistance, currentSpeed = [int(s) for s in raw_input().split(" ")]
        hoursToFinish = (distance-currentDistance)/(currentSpeed*1.00)
        if (hoursToFinish > maxHrs):
            maxHrs = hoursToFinish

    cruisingSpeed = distance/maxHrs

    print("Case #{}: {:.6f}").format(i, cruisingSpeed)
