'''
Author: emmhaych
File Location: /home/emmhaych/Dev/CodeJam/2015/Qualification/A/src/main.py
For license information please refer to LICENSE.txt in the root folder of this project
'''

''' Input/output file names '''
#fileName = 'test'                 # Test input file
#fileName = 'A-small-attempt0'            # Small input file
fileName = 'A-large'            # Large input file

''' Program start location '''
def main():
    # Open input and output files
    inputFile = open('../inputFiles/' + fileName + '.in', 'r')
    outputFile = open('../outputFiles/' + fileName + '.out', 'w+')

    numberOfTestCases = int(inputFile.readline())

    for currentTestCase in range(numberOfTestCases):
        [maxShynessLevel, shynessLevels] = inputFile.readline().split()
        shynessLevels = list(shynessLevels)
        peopleStoodUp = 0
        peopleToAdd = 0
        for currentShynessLevel in range(len(shynessLevels)):
            if(currentShynessLevel > peopleStoodUp) and (int(shynessLevels[currentShynessLevel]) > 0):
                peopleToAdd += currentShynessLevel - peopleStoodUp
                peopleStoodUp += currentShynessLevel - peopleStoodUp
            peopleStoodUp += int(shynessLevels[currentShynessLevel])
        outputFile.write('Case #' + str(currentTestCase + 1) + ': ' + str(peopleToAdd) + '\n')

if __name__ == '__main__':
    main()