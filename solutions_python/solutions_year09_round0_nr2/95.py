import sys

sys.setrecursionlimit(1000)

###############################################################################
# Helper functions                                                            #
###############################################################################
def parseMap(input):
    tmp = input.readline().strip().split()
    h,w = int(tmp[0]), int(tmp[1])

    hMap = []
    for row in range(h):
        line = input.readline().strip().split()
        hMap.append([int(x) for x in line])

    return [h,w,hMap]

def findDrains(hMap,h,w):
    drains = []
    for y in range(h):
        for x in range(w):
            val = hMap[y][x]
            drain = True
            if ((x > 0     and val > hMap[y][x-1]) or # WEST
                (x < (w-1) and val > hMap[y][x+1]) or # EAST
                (y > 0     and val > hMap[y-1][x]) or # NORTH
                (y < (h-1) and val > hMap[y+1][x])):  # SOUTH

                drain = False

            if drain:
                drains.append([y,x])
            
    drains.sort()
    return drains
    
def markLocalDrain(hMap,dMap,done,h,w,y,x,char,rec):
    #rec += 1
    #print "Recursion: " + str(rec) + '(' + str(y) + ',' + str(x) + ')'
    if done[y][x]:
        if dMap[y][x] == '':
            dMap[y][x] = char
        else:
            char = dMap[y][x]
        return char
    else:
        minDir = []
        minVal = 20000
        if y < (h-1) and minVal >= hMap[y+1][x]: # SOUTH
            minDir = [y+1,x]
            minVal = hMap[y+1][x]
        if x < (w-1) and minVal >= hMap[y][x+1]: # EAST
            minDir = [y,x+1]
            minVal = hMap[y][x+1]        
        if x > 0     and minVal >= hMap[y][x-1]: # WEST
            minDir = [y,x-1]
            minVal = hMap[y][x-1]
        if y > 0     and minVal >= hMap[y-1][x]: # NORTH
            minDir = [y-1,x]
            minVal = hMap[y-1][x]

        char = markLocalDrain(hMap,dMap,done,h,w,minDir[0],minDir[1],char,rec)
        dMap[y][x] = char
        done[y][x] = True

        return char

def dMapToString(dMap,h,w):
    string = ''
    for y in range(h):
        for x in range(w):
            if dMap[y][x] == '':
                string += '  '
            else:
                string += dMap[y][x] + ' '
        string += '\r\n'

    return string

def handleCase(hMap, h, w):
    done = [[False for x in range(w)] for y in range(h)] 
    dMap = [['' for x in range(w)]for y in range(h)]

    # Find drains
    drains = findDrains(hMap,h,w)

    # Mark drains
    for drain in drains:
        done[drain[0]][drain[1]] = True

    #print dMapToString(dMap,h,w)

    char = 'a'
    for y in range(h):
        for x in range(w):
            resChar = markLocalDrain(hMap,dMap,done,h,w,y,x,char,0)
            if resChar == char: # New drain
                char = chr(ord(char)+1)
            
    #print dMapToString(dMap,h,w)

    return dMap
    


###############################################################################
# Main                                                                        #
###############################################################################


input  = open(sys.argv[1])
output = open(sys.argv[1].replace('in','out'),'w')
debug  = open(sys.argv[1].replace('in','debug'),'w')

nCases = int(input.readline().strip())

for i in range(nCases):
    [h,w,hMap] = parseMap(input)
    dMap = handleCase(hMap,h,w)

    dMapString = dMapToString(dMap,h,w)
    print "Case #" + str(i+1) + ":"
    #print dMapString,
    output.write("Case #" + str(i+1) + ":\r\n")
    output.write(dMapString)


    
