import re
import sys

def ReadSpecifiedRowFromArrangement(file, rowNumber):
    for i in xrange(1, rowNumber):
        file.readline()
    row = set(file.readline().strip('\n').split(' '))
    for i in xrange(rowNumber, 4):
        file.readline()
    return row

def main():
    inputFile = open(sys.argv[1], "r")
    outputFile = open("output.txt", "w")
    
    casesCount = int(inputFile.readline())
    
    for caseNumber in xrange(1, casesCount + 1):
        firstRowNumber = int(inputFile.readline())
        firstRow = ReadSpecifiedRowFromArrangement(inputFile, firstRowNumber)
        secondRowNumber = int(inputFile.readline())
        secondRow = ReadSpecifiedRowFromArrangement(inputFile, secondRowNumber)
        matches = firstRow & secondRow
        
        outputFile.write("Case #" + str(caseNumber) + ": ")
        if (len(matches) == 0):
            outputFile.write("Volunteer cheated!\n")
        else: 
            if (len(matches) > 1):
                outputFile.write("Bad magician!\n")
            else:
                outputFile.write(str(matches.pop()) + "\n")
        
    inputFile.close()
    outputFile.close()
    
if __name__ == "__main__":
    main()