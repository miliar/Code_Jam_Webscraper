#

T = int(input())
for t in range(T):
    line = input().split()
    smax = int(line[0])
    values = [int(x) for x in line[1]]

    runningCount = 0
    numberToAdd = 0
    for shynessLevel in range(smax + 1):
        #print(shynessLevel, runningCount, numberToAdd)
        if values[shynessLevel] > 0:
            if runningCount - shynessLevel >= 0:
                runningCount += values[shynessLevel]
            else:
                numberToAdd += abs(runningCount - shynessLevel)
                runningCount += abs(runningCount - shynessLevel) + values[shynessLevel]
    print("Case #{0}: {1}".format(t + 1, numberToAdd))
