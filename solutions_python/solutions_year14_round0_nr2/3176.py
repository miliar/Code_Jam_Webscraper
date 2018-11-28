# Google Code Jam 2014 qualification round B.
# Calculate time until buy and time until win.  Stop when time until
# buy plus next time until win is greater than time until win.
import sys

def doCase(file):
    # C, F, X: Cost of farm, rate increase per farm, goal
    (cost, increase, goal) = map(float, file.readline().split())
    rate = 2.                   # Earning 2 per second
    timeSpent = 0.
    while True:
        timeTillGoal = goal/rate # How long to reach goal if we don't buy farm
        timeTillFarm = cost/rate # How long until we can buy a farm
        if timeTillGoal < timeTillFarm + goal / (rate + increase):
            timeSpent += timeTillGoal
            break
        timeSpent += timeTillFarm
        rate += increase
    return timeSpent

def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        answer = doCase(file)
        print 'Case #{0}: {1}'.format(case, answer)
run()
