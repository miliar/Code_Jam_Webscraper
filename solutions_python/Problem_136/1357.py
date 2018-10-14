import sys, os

puzzles = list()

FILENAME = 'B-large.in'

DEFAULT_PRODUCTION = 2.0

def solve(puzzle):
    C, F, X = puzzle
    currentProduction = DEFAULT_PRODUCTION
    currentTime = 0.
    buildingFactories = True
    while buildingFactories:
        timeToCollect = X / currentProduction
        timeToBuildAndCollect = C / currentProduction + X / (currentProduction + F)
        if timeToBuildAndCollect < timeToCollect: #Assume it is better to Collect than Build and Collect (not <=, does not change the end result)
            currentTime += C / currentProduction
            currentProduction += F
        else:
            currentTime += timeToCollect
            buildingFactories = False
    return round(currentTime, 6)



with open(FILENAME, 'r') as f:
    nbTestCases = int(f.readline())
    for _ in range(nbTestCases):
        puzzles.append(float(f) for f in f.readline().strip().split())

printResult = ''
for (i, puzzle) in enumerate(puzzles):
    #print 'Case #%s: %s\n' % (i+1, solve(puzzle))
    printResult += 'Case #%s: %s\n' % (i+1, solve(puzzle))

#print printResult
#sys.exit(0)

if os.path.isfile('result'):
    os.remove('result')
with open('result', 'w') as f:
    f.write(printResult[:-1])