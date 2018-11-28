
import os
import sys



################################################################################


def testWin(character, pattern):

    testPattern = pattern.replace('T', character)
    
    # test rows
    for index in range (0, 4):
        testIndex = index * 4
        if (character == testPattern[testIndex]) and (character == testPattern[testIndex + 1]) and (character == testPattern[testIndex + 2]) and (character == testPattern[testIndex + 3]):
            return True
            
    # test columns
    for index in range(0, 4):
        if (character == testPattern[index]) and (character == testPattern[index + 4]) and (character == testPattern[index + 8]) and (character == testPattern[index + 12]):
            return True
            
    # test diagonals
    if (character == testPattern[0]) and (character == testPattern[5]) and (character == testPattern[10]) and (character == testPattern[15]):
        return True
    if (character == testPattern[3]) and (character == testPattern[6]) and (character == testPattern[9]) and (character == testPattern[12]):
        return True

    return False


def processBoard(caseNumber, entry, outputFile):
    
    result = 'Game has not completed'
    
    if testWin('X', entry):
        result = 'X won'
    elif testWin('O', entry):
        result = 'O won'
    elif not ('.' in entry):
        result = 'Draw'
    
    outputFile.write("Case #" + str(caseNumber) + ': ' + result + "\n")


################################################################################



def processFile(inputFile, outputFile):
    
    input = open(inputFile, 'r')
    output = open(outputFile, 'w')
    
    entry = ''
    caseNumber = 1
    limit = 0
    
    for line in input:
        line = line.rstrip('\r\n')
        
        if (0 == limit):
            limit = int(line)
        elif (0 == len(line)):
            processBoard(caseNumber, entry, output)
            entry = ''
            caseNumber += 1
        else:
            entry = entry + line
    
    if (0 < len(entry)):
        processBoard(caseNumber, entry, output)
    
    output.close()
    input.close()


def main(argv):
    
    processFile(argv[0], argv[1])


if __name__ == '__main__':
    main(sys.argv[1:])