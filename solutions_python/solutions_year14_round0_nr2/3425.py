def main():
    with open('input.txt', 'r') as inputFile:
        outputFile = open("output.txt","w")
        #numberOfTestCases = int(inputFile.readline().rstrip('\n'))
        numberOfTestCases = int(inputFile.readline())
        for testCaseNumber in range(1,numberOfTestCases+1):
            testCaseData = inputFile.readline().rstrip('\n').split(" ")
            defaultCPS = 2
            costOfFarm = float(testCaseData[0])
            farmBonus = float(testCaseData[1])
            requiredCookies = float(testCaseData[2])

            bestTime = requiredCookies / defaultCPS
            numberOfFarms = int(1)
            while True:
                currentTotalFarmBonus = (numberOfFarms * farmBonus)
                currentCPS = currentTotalFarmBonus + defaultCPS
                currentFarmTime = 0
                for i in range(numberOfFarms):
                    currentFarmTime += costOfFarm / ((i*farmBonus) + 2)
                nthTotalTime = currentFarmTime + (requiredCookies/currentCPS)
                #print(numberOfFarms,currentCPS,currentFarmTime,nthTotalTime)
                #print("--------")
                numberOfFarms += 1
                if nthTotalTime < bestTime:
                    bestTime = nthTotalTime
                else:
                    break

            print(bestTime)
            #print("Case #%s: %s" % (testCaseNumber,result))
            outputFile.write("Case #%s: %s\n" % (testCaseNumber,bestTime))

if __name__ == '__main__':
    main()