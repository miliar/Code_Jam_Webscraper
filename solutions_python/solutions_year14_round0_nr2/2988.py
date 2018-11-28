

def parse(filename):
    with open(filename) as f:
        cases = int(f.readline())
        problems = []
        for problem in range(cases):
            line = f.readline()
            problems.append(map(float, line.split(" ")))
        return problems


def solveProblem(problem):
    farmCost, farmSpeed, targetCookies = problem
    currentSpeed = float(2)
    currentTimeTaken = float(0)
    while(True):
        withoutFarmTime = currentTimeTaken + (targetCookies/currentSpeed)
        withFarmTime = currentTimeTaken + (farmCost/currentSpeed) + (targetCookies/(currentSpeed + farmSpeed))

        if (withoutFarmTime < withFarmTime):
            return withoutFarmTime

        currentTimeTaken += farmCost/currentSpeed
        currentSpeed += farmSpeed


def parseAndPrint(filename):
    problems = parse(filename)
    case = 1
    for problem in problems:
        result = solveProblem(problem)
        print "Case #" + str(case) + ": " + str(result)
        case += 1


parseAndPrint("/Users/gcameron/Downloads/B-large.in")