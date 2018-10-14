
import os
import sys



################################################################################


def mowLawn(lawn, row, column, previousMax):
    
    maxHeight = max(lawn)
    
    while (0 < maxHeight):
    
        for index in range(0, len(lawn)):
            
            # for every maximum height, there must either be a mowable ...
            if(maxHeight == lawn[index]):
            
                # ... row
                base = index - (index % column)
                rc = True
                
                for columnindex in range(0, column):
                    if (0 == lawn[columnindex + base]):
                        rc = False
                        break
                
                if rc:
                    continue
                
                # ... or column
                base = index % column
                    
                for rowindex in range(0, row):
                    if (0 == lawn[(rowindex * column) + base]):
                        return False
        
        for index in range(0, len(lawn)):
            if(maxHeight == lawn[index]):
                lawn[index] = 0
                
        maxHeight = max(lawn)
    
    return True

    
################################################################################



def processFile(inputFile, outputFile):
    
    input = open(inputFile, 'r')
    output = open(outputFile, 'w')
    
    entry = ''
    caseNumber = 1
    limit = 0
    
    row = 0
    column = 0
    rowCounter = 0
    
    for line in input:
        line = line.rstrip('\r\n')
        
        if (0 == limit):
            limit = int(line)
        elif (0 == row):
            lines = line.split(' ')
            row = int(lines[0])
            column = int(lines[1])
        else:
            entry = entry + line + ' '
            rowCounter += 1
            
            if (rowCounter == row):
                
                entries = entry.rstrip(' ').split(' ')
                lawn = []
                for index in range(0, len(entries)):
                    lawn.append(int(entries[index]))
                
                if mowLawn(lawn, row, column, -1):
                    output.write("Case #" + str(caseNumber) + ": YES\n")
                else:
                    output.write("Case #" + str(caseNumber) + ": NO\n")
                
                caseNumber += 1
                row = 0
                column = 0
                rowCounter = 0
                entry = ''
        
    output.close()
    input.close()


def main(argv):
    
    processFile(argv[0], argv[1])


if __name__ == '__main__':
    main(sys.argv[1:])