__author__ = 'William Archinal'


def getTable():
    table = []
    for x in xrange(0, 4):
        rowStr = raw_input().split(" ")
        row = []
        for c in rowStr:
            row.append(int(c))
        table.append(row)
    return table


def handleCase(n):
    params = raw_input().split(" ")
    farmCost = float(params[0])
    farmSpeed = float(params[1])
    goal = float(params[2])

    currentBest = 0
    farmsToBuy = 0

    if farmCost >= goal:
        currentBest = goal / 2.0
    else:
        while True:
            timeTaken = 0
            cps = 2.0
            farms = 0
            while farms < farmsToBuy:
                timeTaken += farmCost / cps
                farms += 1
                cps += farmSpeed

            timeTaken += goal / cps


            if timeTaken < currentBest or currentBest is 0:
                currentBest = timeTaken
            else:
                break
            farmsToBuy += 1

    print "Case #" + str(n) + ": " + str("{0:.7f}".format(currentBest))


def main():
    numCases = raw_input()
    for case in xrange(1, int(numCases) + 1):
        handleCase(case)


if __name__ == "__main__":
    main()