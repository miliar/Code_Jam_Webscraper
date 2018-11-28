'''
Created on 31 maj 2010

@author: Jens
'''

fileName = 'C-small-attempt1.in'
#fileName = '3test.txt'
f = open(fileName, 'r')
fOut = open(fileName + 'solution','w')

nrOfCases = int(f.readline()[0:-1])

def hasAOne(field):
    for line in field:
        for pos in line:
            if pos == 1:
                return True
    return False

dim = 200

def getNewMax(field):
    xMax = 0
    yMax = 0
    for y in range(0, len(field)):
        for x in range(0, len(field[y])):
            if(field[y][x] == 1):
                if( x > xMax):
                    xMax = x
                if y > yMax:
                    yMax = y
    return (xMax+2, yMax+2)

def stepField(field):
    newField = []
    
    (xMax,yMax) = getNewMax(field)
    
    for y in range (0,yMax):
        line = []
        for x in range(0, xMax):
            line.append(field[y][x])
            
            #if(x == 0 or y == 0):
                #continue
            
            #If a bacterium has no neighbor to its north and no neighbor to its west, then it will die.
            if (field[y][x-1] == 0 and field[y-1][x] == 0):
                line[x] = 0
            
            #If a cell has no bacterium in it, but there are bacteria in the neighboring cells to the north and to the west, then a new bacterium will be born in that cell. 
            if (field[y][x-1] == 1 and field[y-1][x] == 1 ):
                line[x] = 1
            #else:
                #newField[y][x] = 0
        newField.append(line)
    return newField

for caseNr in range(1, nrOfCases+1):
    result = ''
    
    nrOfRects = int(f.readline()[0:-1])
    
    rects = []
    
    field = []
    for y in range (0, dim):
        line = []
        for x in range (0, dim):
            line.append(0)
        field.append(line)
            
    
    for rect in range(0,nrOfRects):
        rectInfo = f.readline()[0:-1].split(" ")
        
        for x in range(int(rectInfo[0]), int(rectInfo[2]) +1):
            for y in range(int(rectInfo[1]), int(rectInfo[3]) +1):
                field[y][x] = 1
#                print 'setting some 1s'
    
    steps = 0
    
    while(hasAOne(field)):
        field =stepField(field)
        steps += 1
    
    #print field
    
   
    result = str(steps)
    
    print 'Case #' +str(caseNr) + ': ' + result 
    fOut.write('Case #' +str(caseNr) + ': ' + result + '\n')

print 'done'