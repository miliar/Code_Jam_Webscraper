import os, sys, math, time;
startTime = time.time()

# Writes answers for each case to terminal and to output file.
def writeAnswer(outputFile, case, answer):
    line = 'Case #%s: %s' % (case + 1, answer)
    print line
    outputFile.write(line + "\n")

def solveAllCases(fileName):
    print 'Running problem ' + fileName
    inputFile = open(fileName + '.in', 'r')
    outputFile = open(fileName + '.out', 'w')
    cases = int(inputFile.readline())
    print str(cases) + ' cases'
    for case in range(cases):
        print (time.time() - startTime)
        print 'Solving case ' + str(case + 1)
        writeAnswer(outputFile, case, solveCase(inputFile))

def printGrid(grid):
    for row in range(len(grid)):
        print "".join(grid[row])

def solveCase(inputFile):
    answer = '?'
    line = inputFile.readline().split()
    rows = int(line[0])
    columns = int(line[1])
    grid = [['?' for i in range(columns)] for j in range(rows)]
    for row in range(rows):
        line = list(inputFile.readline())
        for column in range(columns):
            grid[row][column] = line[column]

    remainingRectangles = [[0, 0, columns, rows]]
    while (len(remainingRectangles)):
        rectangle = remainingRectangles.pop()
        letters = []
        for row in range(rectangle[1], rectangle[3]):
            for column in range(rectangle[0], rectangle[2]):
                if grid[row][column] == '?':
                    continue
                letters.append([column, row, grid[row][column]])
                if len(letters) > 1:
                    break;
            if len(letters) > 1:
                break;

        if (len(letters) < 2):
            for row in range(rectangle[1], rectangle[3]):
                for column in range(rectangle[0], rectangle[2]):
                    grid[row][column] = letters[0][2]
            continue

        if letters[0][0] != letters[1][0]:
            right = max(letters[0][0], letters[1][0])
            remainingRectangles.append([rectangle[0], rectangle[1], right, rectangle[3]])
            remainingRectangles.append([right, rectangle[1], rectangle[2], rectangle[3]])
        else:
            bottom = max(letters[0][1], letters[1][1])
            remainingRectangles.append([rectangle[0], rectangle[1], rectangle[2], bottom])
            remainingRectangles.append([rectangle[0], bottom, rectangle[2], rectangle[3]])


    answer = "\n"
    for row in range(rows):
        answer += "".join(grid[row]) + "\n"

    # Read input and solve case here, then return the answer.
    return answer[:-1]

solveAllCases('A-large')
