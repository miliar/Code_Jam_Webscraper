def main():
    with open('input.txt', 'r') as inputFile:
        outputFile = open("output.txt","w")
        numberOfTestCases = int(inputFile.readline())
        for testCaseNumber in range(1,numberOfTestCases+1):
            startingRowNumber = int(inputFile.readline())
            startingConfiguration = [inputFile.readline().rstrip('\n').split(" ") for number in range(1,5)]
            endingRowNumber = int(inputFile.readline())
            endingConfiguration = [inputFile.readline().rstrip('\n').split(" ") for number in range(1,5)]
            #print(startingRow,startingConfiguration,endingRow,endingConfiguration)

            startingRowContents = startingConfiguration[startingRowNumber - 1]
            endingRowContents = endingConfiguration[endingRowNumber - 1]
            currentUniqueNumber = None
            result = 'Volunteer cheated!'
            for number in startingRowContents:
                if number in endingRowContents:
                    if currentUniqueNumber == None:
                        currentUniqueNumber = number
                        result = str(currentUniqueNumber)
                    else:
                        result = "Bad magician!"
                        break

            #print("Case #%s: %s" % (testCaseNumber,result))
            outputFile.write("Case #%s: %s\n" % (testCaseNumber,result))

if __name__ == '__main__':
    main()