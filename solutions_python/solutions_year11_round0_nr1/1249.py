count = 0

inputFile = open("C:\Users\Mike\Desktop\A-large.in")
outputFile = open("C:\Users\Mike\Desktop\A-large.txt",'w')

T = int((inputFile.readline().strip()))
while (count < T):
    
    instrList = []
    numOfButtons = 0
    orangePosition = 1
    orangeGoal = 100
    bluePosition = 1
    blueGoal = 100
    currentBot = "O"
    lastBot = "O"
    goalsLeft = 100
    goalColorInList = 1
    numOfSteps = 0
    stepsToGoalButton = 100

    instrList = (inputFile.readline().strip().split())
    numOfButtons = int(instrList[0])
    count = count + 1

    goalsLeft = numOfButtons
    currentBot = instrList[1]

    orangeProgress = 0
    blueProgress = 0
    
    while (goalsLeft != 0):

        if (currentBot == "O"):
            orangeGoal = int(instrList[goalColorInList + 1])
            stepsToGoalButton = abs(orangeGoal - orangePosition)
            if (stepsToGoalButton <= orangeProgress):
                numOfSteps = numOfSteps + 1
                progAdder = 0
            else:
                numOfSteps = numOfSteps + 1 + stepsToGoalButton - orangeProgress
                progAdder = stepsToGoalButton - orangeProgress
            blueProgress = blueProgress + progAdder + 1
            orangeProgress = 0
            orangePosition = orangeGoal
            goalsLeft = goalsLeft - 1
            if (goalsLeft == 0):
                break
            else:
                goalColorInList = goalColorInList + 2
                currentBot = instrList[goalColorInList]
                
        elif (currentBot == "B"):
            blueGoal = int(instrList[goalColorInList + 1])
            stepsToGoalButton = abs(blueGoal - bluePosition)
            if (stepsToGoalButton <= blueProgress):
                numOfSteps = numOfSteps + 1
                progAdder = 0
            else:
                numOfSteps = numOfSteps + 1 + stepsToGoalButton - blueProgress
                progAdder = stepsToGoalButton - blueProgress
            orangeProgress = orangeProgress + progAdder + 1
            blueProgress = 0
            bluePosition = blueGoal
            goalsLeft = goalsLeft - 1

            if (goalsLeft == 0):
                break
            else:
                goalColorInList = goalColorInList + 2
                currentBot = instrList[goalColorInList]
        
            
    result = "Case #%d: %s" % (count, numOfSteps)
    outputFile.write(result)
    if (count < T):
        outputFile.write("\n")
inputFile.close()
outputFile.close()
