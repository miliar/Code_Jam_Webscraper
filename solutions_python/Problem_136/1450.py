import re

def timeNow(C, F, X, numFact, elapsedTime):
    time = X / (2.0 + F * numFact)
    totalTime = time + elapsedTime
    return totalTime
    
def timeNext(C, F, X, numFact, elapsedTime):
    timeForExtraFact = C / (2.0 + F * numFact)
    numFact += 1
    time = X / (2.0 + F * numFact)
    totalTime = time + elapsedTime + timeForExtraFact
    return totalTime, timeForExtraFact

def CookieClicker(inFile):
    f = open('CookieClickerOutput.txt', 'w')
    T = int(inFile.readline()) # number of test cases
    testCase = 1
    while testCase <= T:
        # get my inputs
        inputRow = inFile.readline()
        inputList = re.split(' |\n', inputRow)
        inputList.pop()
        C = float(inputList[0])
        F = float(inputList[1])
        X = float(inputList[2])
    
        elapsedTime = 0
        numFact = 0

        time_now = timeNow(C, F, X, numFact, elapsedTime)

        time_next = timeNext(C, F, X, numFact, elapsedTime)
    
        while time_now > time_next[0]:
            # we want to make one more factory
            timeForExtraFact = time_next[1]
            numFact += 1
            elapsedTime += timeForExtraFact
            
            time_now = timeNow(C, F, X, numFact, elapsedTime)
            time_next = timeNext(C, F, X, numFact, elapsedTime)

        f.write('Case #' + str(testCase) + ':' + ' ' + str(time_now) + '\n')
        testCase += 1
            
