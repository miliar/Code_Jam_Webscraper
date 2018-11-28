import sys

NORTH = 1
WEST = 2
EAST = 4
SOUTH = 8
def printMatrix(mat):
    for line in mat:
        print ' '.join(line)
def makeFlowMap(elevationMap):
    cx = len(elevationMap[0])
    cy = len(elevationMap)
    flowMap = []
    for i in range(cy):
        flowMap.append([0] * cx)
    for y in xrange(cy):
        for x in xrange(cx):
##            print x,y
##            printMatrix(flowMap)
            minAltitude = elevationMap[y][x]
            flowDirect = 0
            ## NORTH
            if y != 0 and minAltitude > elevationMap[y-1][x]:
                minAltitude = elevationMap[y-1][x]
                flowDirect = NORTH
            ## WEST
            if x != 0 and minAltitude > elevationMap[y][x-1]:
                minAltitude = elevationMap[y][x-1]
                flowDirect = WEST
            ## EAST
            if x != (cx - 1) and minAltitude > elevationMap[y][x+1]:
                minAltitude = elevationMap[y][x+1]
                flowDirect = EAST
            ## SOUTH
            if y != (cy - 1) and minAltitude > elevationMap[y+1][x]:
                minAltitude = elevationMap[y+1][x]
                flowDirect = SOUTH
##            print 'flowDirect', flowDirect
            flowMap[y][x] |= flowDirect

            if flowDirect == NORTH:
                flowMap[y-1][x] |= SOUTH
            elif flowDirect == WEST:
                flowMap[y][x-1] |= EAST
            elif flowDirect == EAST:
                flowMap[y][x+1] |= WEST
            elif flowDirect == SOUTH:
                flowMap[y+1][x] |= NORTH
    return flowMap

def flood(flowMap, labelMap, x, y, ch):
    labelMap[y][x] = ch
    if flowMap[y][x] & NORTH == NORTH and labelMap[y-1][x] == None:
        flood(flowMap, labelMap, x, y-1, ch)
    if flowMap[y][x] & WEST == WEST and labelMap[y][x-1] == None:
        flood(flowMap, labelMap, x-1, y, ch)
    if flowMap[y][x] & EAST == EAST and labelMap[y][x+1] == None:
        flood(flowMap, labelMap, x+1, y, ch)
    if flowMap[y][x] & SOUTH == SOUTH and labelMap[y+1][x] == None:
        flood(flowMap, labelMap, x, y+1, ch)
    
def makeLabelMap(flowMap):
    cx = len(flowMap[0])
    cy = len(flowMap)
    labelMap = []
    for i in range(cy):
        labelMap.append([None] * cx)
    curChar = 'a'
    for y in xrange(cy):
        for x in xrange(cx):
            if labelMap[y][x] == None:
                flood(flowMap, labelMap, x, y, curChar);
                curChar = chr(ord(curChar) + 1)
    return labelMap
            

t = int(sys.stdin.readline())
##The number of maps 'T'
##print t 
for i in xrange(t):
    h, w = [int(x) for x in sys.stdin.readline().split()]
##    height and weight    
##    print h,w
    elevationMap =[[]] * h
    for j in xrange(h):
        elevationMap[j] = [int(x) for x in sys.stdin.readline().split()]
##    printMatrix(elevationMap)
    flowMap = makeFlowMap(elevationMap)
##    printMatrix(flowMap)
    labelMap = makeLabelMap(flowMap)
##    printMatrix(labelMap)
    print 'Case #%d:' %(i+1)
    printMatrix(labelMap)
