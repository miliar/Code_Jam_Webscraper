import sys

def ovationComputation (listOfOvations):
    if len(listOfOvations) != 2:
        print 'Wrong format for list of ovations line'
        print 'There were an incorrect number of components at the end of the line'
        sys.exit()
    else:
        # Divide inputs in variables
        maxLevel = int(listOfOvations[0])
        levelsDistributed = listOfOvations[1]

        # Sanity checking, the list of characters does not end in 0
        if levelsDistributed[-1] == '0':
            print 'Given list of shyness ends in 0, it is not properly built'
            sys.exit()

        # Loop through the number of values
        currentLevel = 0
        shynessAchieved = 0
        additionalFriends = 0

        for level in levelsDistributed:
            currentLevelPeople = int(level)

            # Sanity checking, it is between 0 and 9
            if currentLevelPeople > 9 or currentLevelPeople < 0:
                print 'Wrong current shyness level. Given level is not in the [0,9] interval.'
                sys.exit()

            # If there is people I need to launch in the current level
            if currentLevelPeople > 0:
                if shynessAchieved >= currentLevel:
                    shynessAchieved = shynessAchieved + currentLevelPeople
                else:
                    additionalFriends = additionalFriends + currentLevel - shynessAchieved
                    shynessAchieved = shynessAchieved + currentLevelPeople + currentLevel - shynessAchieved

            # Check if we have finished before completing the loop
            if shynessAchieved >= maxLevel:
                break

            currentLevel = currentLevel + 1

        return additionalFriends

def processOvationFile (inputFileName, outputFileName):
    # Read the input file
    origFile = open(inputFileName, 'r')
    allFile = origFile.readlines()

    # Check the number of cases
    solvedCases = 0
    totalNumberCases = int(allFile.pop(0).strip())

    # Process the input file
    caseSolutions = []
    for line in allFile:
        cleanLine = line.strip()

        if len(cleanLine) > 0:
            print 'Processing case ' + str(solvedCases+1) + ' of ' + str(totalNumberCases)
            currentLineValues = cleanLine.split(' ')
            caseSolutions.append('Case #' + str(solvedCases+1) + ': ' + str(ovationComputation(currentLineValues)))
            solvedCases = solvedCases + 1

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
        print 'This script should be called with TWO parameters: python StandingOvation.py <inputFileName> <outputFileName>'
        sys.exit()
    else:
        print 'Processing Ovation File'
        processOvationFile(sys.argv[1], sys.argv[2])