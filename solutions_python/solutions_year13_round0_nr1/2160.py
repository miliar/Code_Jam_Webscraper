import sys

def evaluateDiagonal(grid):
    count = 0
    allx = True
    allo = True
    for line in grid:
        if (line[count] == 'X') | (line[count] == '.'):
            allo = False
        if (line[count] == 'O') | (line[count] == '.'):
            allx = False
        count += 1

    if allx == True:
        return 1
    if allo == True:
        return 2

    count = 3
    allx = True
    allo = True
    for line in grid:
        if (line[count] == 'X') | (line[count] == '.'):
            allo = False
        if (line[count] == 'O') | (line[count] == '.'):
            allx = False
        count -= 1

    if allx == True:
        return 1
    if allo == True:
        return 2
    return 0


def evaluateRow(grid):
    for line in grid:
        allx = True
        allo = True
        for item in line:
            if (item == 'X') | (item == '.'):
                allo = False
            if (item == 'O') | (item == '.'):
                allx = False

        if allx == True:
            return 1
        if allo == True:
            return 2
    return 0

def evaluateColumn(grid):
    count = 0
    while count < 4:
        allx = True
        allo = True
        for line in grid:
            if (line[count] == 'X') | (line[count] == '.'):
                allo = False
            if (line[count] == 'O') | (line[count] == '.'):
                allx = False
                
        if allx == True:
            return 1
        if allo == True:
            return 2
        count += 1
    return 0

def evaluateIncomplete(grid):
    for line in grid:
        if line.count('.') > 0:
            return 3
    return 0

filename = sys.argv[1]
curfile = file(filename, 'rb')
outputfile = file("output2.txt", 'wb')

lines = curfile.readlines()

if lines[0].strip().isdigit():
    numcases = int(lines[0])

count = 0
while count < numcases:
    grid = []
    startline = (count * 5) + 1
    grid.append((lines[startline][0], lines[startline][1], lines[startline][2], lines[startline][3]))
    grid.append((lines[startline + 1][0], lines[startline + 1][1], lines[startline + 1][2], lines[startline + 1][3]))
    grid.append((lines[startline + 2][0], lines[startline + 2][1], lines[startline + 2][2], lines[startline + 2][3]))
    grid.append((lines[startline + 3][0], lines[startline + 3][1], lines[startline + 3][2], lines[startline + 3][3]))

    result = evaluateColumn(grid)
    if result == 1:
        outputfile.write("Case #%i: X won\r\n" % (count+1))
    elif result == 2:
        outputfile.write("Case #%i: O won\r\n" % (count+1))
    else:
        result = evaluateRow(grid)
        if result == 1:
            outputfile.write("Case #%i: X won\r\n" % (count+1))
        elif result == 2:
            outputfile.write("Case #%i: O won\r\n" % (count+1))
        else:
            result = evaluateDiagonal(grid)
            if result == 1:
                outputfile.write("Case #%i: X won\r\n" % (count+1))
            elif result == 2:
                outputfile.write("Case #%i: O won\r\n" % (count+1))
            else:
                result = evaluateIncomplete(grid)
                if result == 3:
                    outputfile.write("Case #%i: Game has not completed\r\n" % (count+1))
                else:
                    outputfile.write("Case #%i: Draw\r\n" % (count+1))
        
    count += 1
    
outputfile.close()



















