def fun(distanceList, horseList):
    stops = len(distanceList)
    # each option looks like [time, remaining distance, speed]
    currentOptions = [(0, horseList[0][0], horseList[0][1])]
    for i in range(1, stops):
        lastOptions = currentOptions
        currentOptions = []
        # new horse
        fastest = -1
        for option in lastOptions:
            if option[1] >= distanceList[i-1]:
                time = option[0] + distanceList[i-1] * 1.0 / option[2]
                if fastest == -1 or time < fastest:
                    fastest = time
        currentOptions.append((fastest, horseList[i][0], horseList[i][1]))
        # no new horse
        for option in lastOptions:
            if option[1] >= distanceList[i-1]:
                time = option[0] + distanceList[i-1] * 1.0 / option[2]
                remainDistance = option[1] - distanceList[i-1]
                currentOptions.append((time, remainDistance, option[2]))
#        print i
#        print currentOptions

    fastest = -1
    for option in currentOptions:
        if option[1] >= distanceList[stops-1]:
            time = option[0] + distanceList[stops-1] * 1.0 / option[2]
            if fastest == -1 or time < fastest:
                fastest = time
    return fastest

n = int(raw_input())
for j in range(n):
    n, q = map(int, raw_input().strip().split(' '))
    horseList = []
    distanceList = []
    for i in range(n):
        horse = map(int, raw_input().strip().split(' '))
        if i != n-1:
            horseList.append(horse)
    for i in range(n):
        distanceMatrix = map(int, raw_input().strip().split(' '))
        if i != n-1:
            distanceList.append(distanceMatrix[i+1])
    for i in range(q):
        odPair = map(int, raw_input().strip().split(' '))
    print "Case #{0}: {1:.7f}".format(j+1, fun(distanceList, horseList))

