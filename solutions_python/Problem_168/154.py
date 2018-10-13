def arrowUp():
    for searchRowIndex in range(0, rowIndex):
        if grid[searchRowIndex][colIndex] != ".":
            return True
            break
    return False

def arrowDown():
    for searchRowIndex in range(rowIndex + 1, rows):
        if grid[searchRowIndex][colIndex] != ".":
            return True
            break
    return False

def arrowLeft():
    for searchColIndex in range(0, colIndex):
        if grid[rowIndex][searchColIndex] != ".":
            return True
            break
    return False

def arrowRight():
    for searchColIndex in range(colIndex + 1, cols):
        if grid[rowIndex][searchColIndex] != ".":
            return True
            break
    return False

import sys

if len(sys.argv) == 1:
    print("No input file provided.")
    sys.exit()
else:
    filename = sys.argv[1]
    try:
        fileobject = open(filename, 'r')
    except:
        print("Failed to open given file.")
        sys.exit()
    try:
        firstLine = fileobject.readline()
    except:
        print("Failed to read first line.")
        sys.exit()
    datasetSize = int(firstLine)
    if not datasetSize:
        print("Unable to parse dataset size.")
        sys.exit()
    lineNr = 1
    for i in range(datasetSize):
        lineNr = lineNr + 1
        try:
            lineText = fileobject.readline()
        except:
            print("Failed to read line ", lineNr)
            sys.exit()
        rowsAndColumns = lineText[0:-1].split(" ")
        rows = int(rowsAndColumns[0])
        cols = int(rowsAndColumns[1])
        grid = []
        for j in range(rows):
            lineNr = lineNr + 1
            try:
                lineText = fileobject.readline()
            except:
                print("Failed to read line ", lineNr)
                sys.exit()
            if lineText[-1] == "\n":
                textToParse = lineText[0:-1]
            else:
                textToParse = lineText
            grid.append(textToParse)
        # If there is an arrow which is in a row and column without other arrows,
        # keeping pegman in the grid is impossible.
        possible = True
        turnsRequired = 0
        for rowIndex in range(len(grid)):
            for colIndex in range(len(grid[rowIndex])):
                if grid[rowIndex][colIndex] != ".":
                    possible = arrowUp() or arrowDown() or arrowLeft() or arrowRight()
                    if not possible:
                        break
        if possible:
            # Find arrows which point of the map and turn them so the point to a
            # different arrow.
            for rowIndex in range(len(grid)):
                for colIndex in range(len(grid[rowIndex])):
                    if grid[rowIndex][colIndex] == ".":
                        continue
                    elif grid[rowIndex][colIndex] == "^":
                        if not arrowUp():
                            turnsRequired += 1
                    elif grid[rowIndex][colIndex] == ">":
                        if not arrowRight():
                            turnsRequired += 1
                    elif grid[rowIndex][colIndex] == "v":
                        if not arrowDown():
                            turnsRequired += 1
                    elif grid[rowIndex][colIndex] == "<":
                        if not arrowLeft():
                            turnsRequired += 1
        output = ""
        if possible:
            output = str(turnsRequired)
        else:
            output = "IMPOSSIBLE"
        if i == 0:
            startCharacter = ""
        else:
            startCharacter = "\n"
        print(startCharacter, "Case #", i+1, ": ", output, end="", sep="")
