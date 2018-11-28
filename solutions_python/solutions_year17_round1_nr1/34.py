from __future__ import print_function
import sys

# print to stderr for debugging
enableDebug = False
def printe(*stuff):
    if enableDebug:
        print(*stuff, file=sys.stderr) 


# Open file for processing
filename = sys.argv[1]
inputFile = open(filename, 'r')
lines = [l.rstrip('\n') for l in inputFile]
linesIter = iter(lines)
nCases = int(linesIter.next())


# Process each case
for iCase in range(1,nCases+1):
    printe("\nProcessing case " + str(iCase))

    items = linesIter.next().split()
    nRows = int(items[0])
    nCols = int(items[1])


    # Solve problem
    grid = []
    for iRow in range(nRows):
        line = linesIter.next().strip()
        grid.append(list(line))


    # Fill every row greedily
    for iRow in range(nRows):
        
        firstChar = "-"
        for iCol in range(nCols):
            if grid[iRow][iCol] != "?":
                firstChar = grid[iRow][iCol]
                break

        
        if(firstChar == "-"):
            continue

        currChar = firstChar
        for iCol in range(nCols):
            if grid[iRow][iCol] == "?":
                grid[iRow][iCol] = currChar 
            else:
                currChar = grid[iRow][iCol]
    
    # Fill every col greedily
    for iCol in range(nCols):
        
        firstChar = "-"
        for iRow in range(nRows):
            if grid[iRow][iCol] != "?":
                firstChar = grid[iRow][iCol]
                break
        
        if(firstChar == "-"):
            continue

        currChar = firstChar
        for iRow in range(nRows):
            if grid[iRow][iCol] == "?":
                grid[iRow][iCol] = currChar 
            else:
                currChar = grid[iRow][iCol]


    print("Case #{}:".format(iCase))
    for row in grid:
        print("".join(row))
