def getInputAndCalculate(inputFile):
    file = open(inputFile)
    fileLines = file.readlines()
    file.close()
    numberOfTests = int(fileLines[0].strip()) 
    output = []
    for i in range(1,numberOfTests+1):
        line = [float(x) for x in fileLines[i].split()]
        cost = line[0]
        increase = line[1]
        target = line[2]
        answer = solveCookieProblem(cost,increase,target)
        output.append("Case #" + str(i) + ": " + answer + "\n")
        outputFile = open("outputFile.txt","w")
        outputFile.writelines(output)
        outputFile.close()

def solveCookieProblem(cost,increase,target):
    currentTimeTaken = 0.0
    cookiesPerSecond = 2.0
    buildAnotherFarm = True
    while(buildAnotherFarm):
        timeUnderCurrent = target / cookiesPerSecond
        potentialCookiesPerSecond = cookiesPerSecond + increase
        timeToNextFarm = cost / cookiesPerSecond
        timeToFuture = timeToNextFarm + (target / potentialCookiesPerSecond)
        if (timeToFuture < timeUnderCurrent):
            currentTimeTaken = currentTimeTaken + (cost / cookiesPerSecond)
            cookiesPerSecond = cookiesPerSecond + increase
        else:
            currentTimeTaken = currentTimeTaken + (target / cookiesPerSecond)
            buildAnotherFarm = False
    currentTimeTaken = round(currentTimeTaken,7)
    return str(currentTimeTaken)
