
FILE = open("A-small-attempt2-2.in","r")
OUTPUT = open("A-small-attempt2-2.out","w")

cases = FILE.readline()

for i in range(0,int(cases)):
    temp = FILE.readline().split(" ")
    gridSize = int(temp[0])
    lengthNeeded = int(temp[1])
    grid = []
    for j in range(0,gridSize):
        gridLine = FILE.readline()
        empty = ''
        values = ''
        for k in range(0,gridSize):
                if gridLine[k] is not '.':
                    values = values + gridLine[k]
                else:
                    empty = "." + empty
        grid.append(empty + values)
    bluePossible = False
    redPossible = False
    for j in range(0,gridSize):
        count = 0
        value = "B"
        gridLine = grid[j]
        for k in range(0,gridSize):
            if gridLine[k] is value:
                count += 1
                if count == lengthNeeded:
                    if value is "B":
                      bluePossible = True  
                    else:
                      redPossible = True
            elif gridLine[k] is not ".":
                value = gridLine[k]
                count = 1
    for j in range(0,gridSize):
        count = 0
        value = "B"
        for k in range(0,gridSize):
            if grid[k][j] is value:
                count += 1
                if count == lengthNeeded:
                    if value is "B":
                      bluePossible = True  
                    else:
                      redPossible = True
            elif grid[k][j] is not ".":
                value = grid[k][j]
                count = 1
    for j in range(0,gridSize - lengthNeeded+1):
        count = 0
        value = "B"
        for k in range(0,gridSize-j):
            if grid[k + j][k] is value:
                count += 1
                if count == lengthNeeded:
                    if value is "B":
                      bluePossible = True  
                    else:
                      redPossible = True
            elif grid[k+j][k] is not ".":
                value = grid[k+j][k]
                count = 1
    for j in range(0,gridSize - lengthNeeded+1):
        count = 0
        value = ""
        for k in range(0,gridSize-j):
            if grid[k+j][gridSize - k - 1] is value:
                count += 1
                if count == lengthNeeded:
                    if value is "B":
                      bluePossible = True  
                    else:
                      redPossible = True
            elif grid[k+j][gridSize - k - 1] is not ".":
                value = grid[k+j][gridSize - k - 1]
                count = 1
    for j in range(0,gridSize - lengthNeeded+1):
        count = 0
        value = ""
        for k in range(0,gridSize-j):
            if grid[k][j+k] is value:
                count += 1
                if count == lengthNeeded:
                    if value is "B":
                      bluePossible = True  
                    else:
                      redPossible = True
            elif grid[k][j+k] is not ".":
                value = grid[j][j+k]
                count = 1
    for j in range(0,gridSize - lengthNeeded+1):
        count = 0
        value = ""
        for k in range(0,gridSize-j):
            if grid[gridSize - k - 1][k+j] is value:
                count += 1
                if count == lengthNeeded:
                    if value is "B":
                      bluePossible = True  
                    else:
                      redPossible = True
            elif grid[gridSize - k - 1][k+j] is not ".":
                value = grid[gridSize - k - 1][k+j]
                count = 1

    writeValue = "Case #" + str(i+1) + ": "
    if redPossible and bluePossible:
        writeValue = writeValue + "Both"
    elif redPossible:
        writeValue = writeValue + "Red"
    elif bluePossible:
        writeValue = writeValue + "Blue"
    else:
        writeValue = writeValue + "Neither"
    
    OUTPUT.write(writeValue + '\n')

FILE.close()
OUTPUT.close()

