import sys, math

def pancakesComputation (activeProcessors, listOfProcessors):
    if activeProcessors == 1:
        if listOfProcessors[0] <= 3:
            return listOfProcessors[0]
        else:
            minSpan = listOfProcessors[0]

            largest = int(math.ceil(math.sqrt(listOfProcessors[0])))+1
            for i in range(2,largest):
                value1 = int(math.ceil(listOfProcessors[0]/float(i)))
                value2 = listOfProcessors[0] - value1
                splitComputation = 1+pancakesComputation(activeProcessors+1, [value1,value2])
                if splitComputation < minSpan:
                    minSpan = splitComputation

            return minSpan
    else:
        # Following a greedy algorithm, we split over the highest value
        posMax = listOfProcessors.index(max(listOfProcessors))

        if listOfProcessors[posMax] <= 3:
            return listOfProcessors[posMax]

        minSpan = listOfProcessors[posMax]
        largest = int(math.ceil(math.sqrt(listOfProcessors[posMax])))+1
        for i in range(2,largest):
            value1 = int(math.ceil(listOfProcessors[posMax]/float(i)))
            value2 = listOfProcessors[posMax] - value1
            newList = listOfProcessors[0:posMax] + [value1,value2] + listOfProcessors[(posMax+1):len(listOfProcessors)]

            splitComputation = 1 + pancakesComputation(activeProcessors+1, newList)
            if splitComputation < minSpan:
                minSpan = splitComputation

        return minSpan

def processPancakesFile (inputFileName, outputFileName):
    # Read the input file
    origFile = open(inputFileName, 'r')
    allFile = origFile.readlines()

    # Check the number of cases
    solvedCases = 0
    totalNumberCases = int(allFile.pop(0).strip())

    # Process the input file
    caseSolutions = []
    readLine = [True] * len(allFile)
    currentLine = 0

    for line in allFile:
        if readLine[currentLine]:
            cleanLine = line.strip()

            if len(cleanLine) > 0:
                print 'Processing case ' + str(solvedCases+1) + ' of ' + str(totalNumberCases)

                # Get the data of the case
                activeProcessors = int(cleanLine)
                nextLine = currentLine+1
                cleanLine = allFile[nextLine].strip()
                readLine[nextLine] = False
                while len(cleanLine) == 0:
                    nextLine = nextLine+1
                    cleanLine = allFile[nextLine].strip()
                    readLine[nextLine] = False

                resourcesToProcess = [int(n) for n in cleanLine.split(' ')]

                if len(resourcesToProcess) != activeProcessors:
                    print 'Wrong format for list of processing pancakes'
                    print 'There is an incorrect number of components in the second line'
                    sys.exit()

                caseSolutions.append('Case #' + str(solvedCases+1) + ': ' + str(pancakesComputation(activeProcessors, resourcesToProcess)))
                solvedCases = solvedCases + 1

        currentLine = currentLine + 1

    if solvedCases != totalNumberCases:
        print 'Number of solved cases does not match the number of total cases'
        print 'Number of total cases is ' + str(totalNumberCases)
        print 'Number of solved cases is ' + str(solvedCases)

    # Open output file
    secondOutput = open(outputFileName, 'w')
    secondOutput.write('\n'.join(caseSolutions))
    secondOutput.close()

# Process the ovation input file to the program
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Incorrect number of arguments given to the script.'
        print 'This script should be called with TWO parameters: python InfinitePancakes.py <inputFileName> <outputFileName>'
        sys.exit()
    else:
        print 'Processing Pancakes File'
        processPancakesFile(sys.argv[1], sys.argv[2])
