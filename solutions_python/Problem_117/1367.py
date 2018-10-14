f = open('B-large.in')
g = open('B-large.txt', 'w')
numCases = f.readline()

def checkLayout(grid, lineNM):
    currX = 0
    currY = 0
    while True:
        currValue = int(grid[currY][currX])
        canEnter = True
        for i in xrange(int(lineNM[1])):
            if int(grid[currY][i]) > currValue:
                canEnter = False
        if not canEnter:
            canEnter = True
            for i in xrange(int(lineNM[0])):
                if int(grid[i][currX]) > currValue:
                    canEnter = False
        if not canEnter:
            return False
        currX += 1
        if currX + 1 > int(lineNM[1]) and currY + 1 < int(lineNM[0]):
            currX = 0
            currY += 1
        elif currX + 1 > int(lineNM[1]) and currY + 1 == int(lineNM[0]):
            return True


for i in range(int(numCases)):
    lineNM = f.readline().split()
    grassLayout = []
    for b in range(int(lineNM[0])):
        grassLayout.append(f.readline().split())
    if checkLayout(grassLayout, lineNM):
        g.write('Case #{}: YES'.format(i + 1))
    else:
        g.write('Case #{}: NO'.format(i + 1))
    g.write('\n')
f.close()
g.close()
