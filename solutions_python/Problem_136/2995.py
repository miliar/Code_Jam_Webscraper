import sys
import logging

def HandleCase():
    farms = 0
    elapsed = timeToGoal = 0.0

    while True:
        timeToGoal = elapsed + TimeNeeded(farms, cookiesNeeded)
        timeToFarm = TimeNeeded(farms, costOfFarm)
        timeToGoalWithExtraFarm = elapsed + timeToFarm + \
            TimeNeeded(farms+1, cookiesNeeded)
        logging.debug('timetogoal: {0:0.07f}'.format(timeToGoal))
        logging.debug('timetogoalwithextrafarm: {0:0.07f}'.format(
            timeToGoalWithExtraFarm))

        if timeToGoal < timeToGoalWithExtraFarm:
            elapsed = timeToGoal
            break;

        elapsed = elapsed + timeToFarm
        farms = farms + 1
        logging.debug('elapsed: {0:0.07f}'.format(elapsed))

    return elapsed

def TimeNeeded(farms, cookiesNeeded):
    cookiesPerSecond = baseCookiesPerSecond + (farms * cookiesPerFarm)
    return cookiesNeeded / cookiesPerSecond

def OutputSingleCase(x, y):
    print "Case #{0}: {1:0.7f}".format(x, y)

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

baseCookiesPerSecond = 2.0
cookiesPerFarm = costOfFarm = cookiesNeeded = 0.0

inp = file('input.txt', 'r')

numberOfCases = int(inp.readline())

for case in range(1, numberOfCases+1):
    costOfFarm, cookiesPerFarm, cookiesNeeded = \
        [float(x) for x in inp.readline().rstrip().split(' ')]
    logging.debug('case input: {0} {1} {2}'.format(
        costOfFarm, cookiesPerFarm, cookiesNeeded))

    minimumSecondsToGoal = HandleCase()
    OutputSingleCase(case, minimumSecondsToGoal)

