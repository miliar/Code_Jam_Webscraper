def loadGrid(fh):
    grid = []
    for eachRow in range(0,4):
        eachLine = fh.readline().strip()
        gridLine = []
        for eachChar in eachLine:
            gridLine.append(eachChar)
        grid.append(gridLine)
    return grid

def compareChar(chars):
    if (chars[0] == '.' or chars[1] == '.' or chars[2] == '.' or chars[3] == '.'):
        return False, ''
    countX = 0
    countO = 0
    countT = 0
    for eachChar in chars:
        if eachChar == 'X':
            countX += 1
        elif eachChar == 'O':
            countO += 1
        elif eachChar == 'T':
            countT += 1
    if countX + countT == 4:
        return True, 'X'
    elif countO + countT == 4:
        return True, 'O'
    else:
        return False, ''
    
def determineState(grid):
    #horizontal
    for eachRow in grid:
        resultCompare, charCompare = compareChar(eachRow)
        if resultCompare:
            return charCompare

    #vertical
    for eachCol in range(0,4):
        eachSet = []
        for eachRow in range(0,4):
            eachSet.append(grid[eachRow][eachCol])
        resultCompare, charCompare = compareChar(eachSet)
        if resultCompare:
            return charCompare
			
    #diag
    eachSet = []
    for eachDot in range(0,4):
        eachSet.append(grid[eachDot][eachDot])
    resultCompare, charCompare = compareChar(eachSet)
    if resultCompare:
        return charCompare
    
    #diag2
    eachSet = []
    for eachDot in range(0,4):
        eachSet.append(grid[3 - eachDot][eachDot])
    resultCompare, charCompare = compareChar(eachSet)
    if resultCompare:
        return charCompare

    #notgood
    for eachLine in grid:
        for eachChar in eachLine:
            if eachChar == '.':
                return 4 #ongoing
    return 3 #draw
    
def main():
    fh = open("input.txt", 'r')
    output = open("output.txt", 'w')
    numCase = int(fh.readline())
    message = ''
    for eachCase in range(0,numCase):
        grid = loadGrid(fh)
        result = determineState(grid)
        if result == 3:
            message = "Draw"
        elif result == 4:
            message = "Game has not completed"
        else:
            message = result + " won"
            
        output.write("Case #")
        output.write(str(eachCase+1))
        output.write(": ")
        output.write(message)
        output.write('\n')
        
        fh.readline()
    fh.close()
    output.close()

main()
