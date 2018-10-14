import re

curChar = 96
map = []
xsize = ysize = 0

def getNextChar():
    global curChar
    curChar += 1
    return chr( curChar )
    
def getGroupOfLowestNeighbor(x, y):
    
    if map[x][y][1] != '?':
        return map[x][y][1]
    
    lowest = map[x][y][0]
    lowx = -1
    lowy = -1
    if x > 0 and map[x-1][y][0] < lowest:
        lowest = map[x-1][y][0]
        lowx = x-1
        lowy = y
    if y > 0 and map[x][y-1][0] < lowest:
        lowest = map[x][y-1][0]
        lowx = x
        lowy = y-1
    if y+1 < ysize and map[x][y+1][0] < lowest:
        lowest = map[x][y+1][0]
        lowx = x
        lowy = y+1
    if x+1 < xsize and map[x+1][y][0] < lowest:
        lowest = map[x+1][y][0]
        lowx = x+1
        lowy = y
    
    if lowest == map[x][y][0]:
        map[x][y][1] = getNextChar()
        return map[x][y][1]

    map[x][y][1] = getGroupOfLowestNeighbor(lowx, lowy)
    return map[x][y][1]
  

f = open('B-large.in')
N = int(f.readline())

for i in range(0, N):
    curChar = 96
    xsize, ysize = f.readline().split()
    xsize = int(xsize)
    ysize = int(ysize)
    map = []
    for j in range(0, xsize):
        map.append( [] )
        numbers = f.readline().split()
        for num in numbers:
            map[j].append( [int(num), '?', 10000] )
    sources = [] 
    for x in range(0, xsize):
        for y in range(0, ysize):
            if map[x][y][1] == '?':
                map[x][y][1] = getGroupOfLowestNeighbor(x, y)

        
    print "Case #%d:" % (i+1)
    for line in map:
        for cell in line:
            print cell[1],
        print

