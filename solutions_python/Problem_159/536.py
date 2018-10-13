def biggestDifference(l):
    case = l
    maxDifference = 0
    for period in xrange(0, len(case) - 1):
        periodDiff = case[period] - case[period + 1]
        if (periodDiff > maxDifference):
            maxDifference = periodDiff
    return maxDifference

mushin = open('mushroom.in', 'r')
mushout = open('mushroom.out', 'w')

numberCases = int(mushin.readline())

for case in xrange(0, numberCases):
    numberIntervals = int(mushin.readline())
    test = map(int, mushin.readline().split())
    methodOneCount = 0                                  # Method 1
    maxDiff = biggestDifference(test)                   # Method 2
    methodTwoCount = 0

    for period in xrange(0, len(test) - 1):
        periodDiff = test[period] - test[period + 1]
        if (periodDiff > 0):
            methodOneCount += periodDiff

    for period in xrange(0, len(test) - 1):
        eat = test[period] - maxDiff
        if (eat < 0):
            methodTwoCount += test[period]
        else:
            methodTwoCount += maxDiff

    mushout.write('Case #' + str(case + 1) + ': ' + str(methodOneCount) + ' ' + str(methodTwoCount) + '\n')