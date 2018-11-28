from collections import defaultdict
import sys
import copy

def testCase(gridSize):
    row = '-' * gridSize
    grid = [row] * gridSize
    print "\n".join(grid)


def valid(grid):
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == "/":
                return False
    for x in range(len(grid)):
        count = 0
        pluscount = 0
        for y in range(len(grid)):
            if grid[x][y] != ".":
                count += 1
            if grid[x][y] == "+":
                pluscount +=1
        if count >= 2 and pluscount < count - 1:
            #print x
            #print "4", count, pluscount
            return False

    for y in range(len(grid)):
        count = 0
        pluscount = 0
        for x in range(len(grid)):
            if grid[x][y] != ".":
                count += 1
            if grid[x][y] == "+":
                pluscount +=1
        if count >= 2 and pluscount < count - 1:
            #print y
            #print "3", count, pluscount
            return False

    for x in range(len(grid)):
        y = 0
        count = 0
        xcount = 0
        for x2 in range(x, len(grid)):
            #print 'x', x, x2, y
            if grid[x2][y] != ".":
                count += 1
            if grid[x2][y] == "x":
                xcount +=1
            y += 1
        if count >= 2 and xcount < count - 1:
            #print x
            #print "2", count, xcount
            return False

    for x in range(len(grid)):
        y = len(grid) - 1
        count = 0
        xcount = 0
        for x2 in range(x, len(grid)):
            #print 'x', x, x2, y
            if grid[x2][y] != ".":
                count += 1
            if grid[x2][y] == "x":
                xcount +=1
            y -= 1
        if count >= 2 and xcount < count - 1:
            #print x
            #print "2", count, xcount
            return False



    for y in range(len(grid)):
        x = 0
        count = 0
        xcount = 0
        for y2 in range(y, len(grid)):
            #print 'y',x, y2, y
            if grid[x][y2] != ".":
                count += 1
            if grid[x][y2] == "x":
                xcount +=1
            x += 1
        if count >= 2 and xcount < count - 1:
            #print y
            #print "1", count, xcount
            return False

    for y in range(len(grid)):
        x = 0
        count = 0
        xcount = 0
        for y2 in range(y, -1,-1):
            #print 'y',x, y2, y
            if grid[x][y2] != ".":
                count += 1
            if grid[x][y2] == "x":
                xcount +=1
            x += 1
        if count >= 2 and xcount < count - 1:
            #print y
            #print "1", count, xcount
            return False




    #print valid
    #print "\n".join(["".join(a) for a in grid])
    return True


def score(grid):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == "/":
                return 0
            if grid[x][y] == "x":
                count += 1
            if grid[x][y] == ".":
                count += 0
            if grid[x][y] == "+":
                count += 1
            if grid[x][y] == "o":
                count += 2
    return count

maxValue = 0
grids = []

def better(grid):
    global maxValue
    global grids
    if gridCounts(grid):
        value = score(grid)
        if value > maxValue:
            maxValue = value
            grids = [copy.deepcopy(grid)]
            #print "Valid", score(grid)
            #print "\n".join(["".join(a) for a in grid])
        elif value == maxValue:
            grids.append(copy.deepcopy(grid))

def gridCounts(grid):
    print "\n".join(["".join(a) for a in grid])
    print "Maybe"
    #[rowCount, plusCount],[columnCount, pluscount],[diagonalCount, xCount],[diagonalCount, xCount]
    counts = [[[0,0] for x in range(len(grid))],[[0,0] for x in range(len(grid))],[[0,0] for x in range(len(grid)*2-1)],[[0,0] for x in range(len(grid)*2-1)]]
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] != ".":
                counts[0][x][0] += 1
                counts[1][y][0] += 1
                counts[2][x-y + len(grid)-1][0] += 1
                counts[3][x-y][0] += 1
            if grid[x][y] == "+":
                counts[0][x][1] += 1
                counts[1][y][1] += 1
            if grid[x][y] == "x":
                counts[2][x-y + len(grid)-1][1] += 1
                counts[3][x+y][1] += 1
    #print counts
    for i, item in enumerate(counts):
        for j, row in enumerate(item):
            if row[1] < row[0] - 1:
                print i,j, row
                return False
    print "Yes"
    return True


def genHelper(grid, size, x, y):
    #print "test", x, y, size
    #print "\n".join(["".join(a) for a in grid])
    if x >= size or y >= size or y < 0 or x < 0:
        return False
    if grid[x][y] != '/':
        return False
    for value in ['.','+','o','x']:
        grid[x][y] = value
        better(grid)
        '''genHelper(copy.deepcopy(grid), size, x+1, y)
        genHelper(copy.deepcopy(grid), size, x, y+1)
        genHelper(copy.deepcopy(grid), size, x-1, y)
        genHelper(copy.deepcopy(grid), size, x, y-1)'''
        genHelper(grid, size, x+1, y)
        genHelper(grid, size, x, y+1)
        genHelper(grid, size, x-1, y)
        genHelper(grid, size, x, y-1)
    grid[x][y] = "/"


def genHelper2(grid, size):
    #[rowCount, plusCount],[columnCount, pluscount],[diagonalCount, xCount],[diagonalCount, xCount]
    counts = [[[0,0] for x in range(len(grid))],[[0,0] for x in range(len(grid))],[[0,0] for x in range(len(grid)*2-1)],[[0,0] for x in range(len(grid)*2-1)]]
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] != ".":
                counts[0][x][0] += 1
                counts[1][y][0] += 1
                counts[2][x-y + len(grid)-1][0] += 1
                counts[3][x+y][0] += 1
            if grid[x][y] == "+":
                counts[0][x][1] += 1
                counts[1][y][1] += 1
            if grid[x][y] == "x":
                counts[2][x-y + len(grid)-1][1] += 1
                counts[3][x+y][1] += 1
    #print counts
    for i, item in enumerate(counts):
        for j, row in enumerate(item):
            if row[0] >= row[0] + 1:
                print i,j, row
                return False

    for x in [0,len(grid)-1] + range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == ".":
                '''print x,y
                print counts
                print "\n".join(["".join(a) for a in grid])'''
                handleX = True
                handlePlus = True
                #Skip in first Loop
                handleO = False
                if counts[0][x][0] >= counts[0][x][1] + 1:
                    #Maximum Non + in row
                    handleX = False
                    handleO = False

                if counts[1][y][0] >= counts[1][y][1] + 1:
                    #Maximum Non + in column
                    handleX = False
                    handleO = False

                if counts[2][x-y + len(grid)-1][0] >= counts[2][x-y + len(grid)-1][1] + 1:
                    #Maximum Non X in column
                    handlePlus = False
                    handleO = False

                if counts[3][x+y][0] >= counts[3][x+y][1] + 1:
                    #Max non X in diagonal
                    handlePlus = False
                    handleO = False

                if handleO:
                    grid[x][y]= 'o'
                    counts[0][x][0] += 1
                    counts[1][y][0] += 1
                    counts[2][x-y + len(grid)-1][0] += 1
                    counts[3][x+y][0] += 1
                elif handlePlus:
                    grid[x][y]= '+'
                    counts[0][x][0] += 1
                    counts[1][y][0] += 1
                    counts[2][x-y + len(grid)-1][0] += 1
                    counts[3][x+y][0] += 1

                    counts[0][x][1] += 1
                    counts[1][y][1] += 1
                elif handleX:
                    grid[x][y]= 'x'
                    counts[0][x][0] += 1
                    counts[1][y][0] += 1
                    counts[2][x-y + len(grid)-1][0] += 1
                    counts[3][x+y][0] += 1

                    counts[2][x-y + len(grid)-1][1] += 1
                    counts[3][x+y][1] += 1

            if grid[x][y] == "+" or grid[x][y] == "x":
                handleO = False
                '''print grid[x][y]
                print x,y
                print counts
                print "\n".join(["".join(a) for a in grid])

                print counts[0][x]
                print counts[1][y]
                print counts[2][x-y + len(grid)]
                print counts[3][x+y]'''
                if grid[x][y] == "+":
                    handleO = False
                    if counts[0][x][0] == counts[0][x][1] and counts[1][y][0] == counts[1][y][1]:
                        grid[x][y]= 'o'
                        counts[0][x][1] -= 1
                        counts[1][y][1] -= 1


                if grid[x][y] == "x":
                    handleO = False
                    if counts[2][x-y + len(grid)-1][0] == counts[2][x-y + len(grid)-1][1] and counts[3][x+y][0] == counts[3][x+y][1]:
                        grid[x][y]= 'o'
                        counts[2][x-y + len(grid)-1][1] -= 1
                        counts[3][x+y][1] -= 1

    #print counts
    return grid


    '''

    #assume is valid
    #print "test", x, y, size
    #print "\n".join(["".join(a) for a in grid])
    if x >= size or y >= size or y < 0 or x < 0:
        return False
    if grid[x][y] != '.':
        return False
    for value in ['+','o','x']:
        grid[x][y] = value
        #print "test", x, y, size
        #print "\n".join(["".join(a) for a in grid])
        count = 0
        pluscount = 0
        for y2 in range(len(grid)):
            if grid[x][y2] != ".":
                count += 1
            if grid[x][y2] == "+":
                pluscount +=1
        if count >= 2 and pluscount < count - 1:
            continue

        count = 0
        pluscount = 0
        for x2 in range(len(grid)):
            if grid[x2][y] != ".":
                count += 1
            if grid[x2][y] == "+":
                pluscount +=1
        if count >= 2 and pluscount < count - 1:
            continue

        count1 = 0
        xcount1 = 0
        count2 = 0
        xcount2 = 0
        for x2 in range(len(grid)):
            for y2 in range(len(grid)):
                if x2 + y2 == x + y:
                    if grid[x2][y2] != ".":
                        count1 += 1
                    if grid[x2][y2] == "x":
                        xcount1 +=1
                if x2 - y2 == x - y:
                    if grid[x2][y2] != ".":
                        count2 += 1
                    if grid[x2][y2] == "x":
                        xcount2 +=1
        if count1 >= 2 and xcount1 < count1 - 1:
            continue
        if count2 >= 2 and xcount2 < count2 - 1:
            continue

        better(grid)
        genHelper2(grid, size, x+1, y)
        genHelper2(grid, size, x, y+1)
        genHelper2(grid, size, x-1, y)
        genHelper2(grid, size, x, y-1)
    grid[x][y] = '.'''



def maxValueCalc(size):
    global maxValue
    global grids
    #grid = [['/'] * size] * size
    grid = [['.' for y in range(0,size)] for x in range(0,size)]
    grid = copy.deepcopy(grid)
    maxValue = 0
    grids = []

    grid = genHelper2(grid, size)


    print "Valid", score(grid)
    print "\n".join(["".join(a) for a in grid])
'''for i in range(6):
    maxValueCalc(i)


sys.exit(1)'''
testcount = int(sys.stdin.readline())
for j in range(testcount):
    line = sys.stdin.readline()
    values = map(int, line.split(" "))
    gridSize = values[0]
    grid = [['.' for y in range(0,gridSize)] for x in range(0,gridSize)]
    for i in range(values[1]):
        coordline = sys.stdin.readline().strip("\n").split(" ")
        #print coordline
        grid[int(coordline[1])-1][int(coordline[2])-1] = coordline[0]
    origGrid = copy.deepcopy(grid)
    debug = 0
    if debug: print "Start"
    if debug: print "\n".join(["".join(a) for a in grid])
    newGrid = genHelper2(grid, gridSize)
    if debug: print "Valid", score(newGrid)
    if debug: print "\n".join(["".join(a) for a in newGrid])

    changes = []
    for x in range(len(grid)):
        for y in range(len(grid)):
            if newGrid[x][y] != origGrid[x][y]:
                changes.append([newGrid[x][y],x,y])

    print("Case #{}: {} {}".format(j+1, score(newGrid), len(changes)))
    if not debug:
        for change in changes:
            print("{} {} {}".format(change[0], change[1] +1, change[2] +1))
