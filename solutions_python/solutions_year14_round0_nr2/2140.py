with open('cookieIN') as infile:
    content = infile.readlines()
    for i in range(0, int(content[0])):
        [C, F, X] = [float(j) for j in content[i+1].split(' ')]
        currentRate = 2
        timeUsed = 0
        timeToNextFarm = C/currentRate
        timeToGoal = X/currentRate
        timeToGoalWithNextFarm = X/(currentRate+F)
        while timeToNextFarm + timeToGoalWithNextFarm < timeToGoal:
            timeUsed += timeToNextFarm
            currentRate += F
            timeToNextFarm = C/currentRate
            timeToGoal = X/currentRate
            timeToGoalWithNextFarm = X/(currentRate+F)
        timeUsed += timeToGoal
        print('Case #{0}: {1:.7f}'.format(str(i+1), timeUsed))
