import sys,math

#self explained
sys.setrecursionlimit(10000)

def printMap(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            sys.stdout.write(map[i][j])
        print ""

def copyMap(map):
    new = []
    for i in range(len(map)):
        new.append([])
        for j in range(len(map[0])):
            new[i].append(map[i][j])
    return new

def howManyMinesNearby(map,x,y):
    mines = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i==j and i==0 or x+i<0 or y+j<0 or x+i>=len(map) or y+j >= len(map[0]):
                continue;
            if map[x+i][y+j] == '*':
                mines+=1
    return mines


def newMap():
    map = []
    for i in range(r):
        map.append([])
        for j in range(c):
            map[i].append('*')
    return map


def propagate(map,x,y):
    spaces_placed = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i==j and i==0 or x+i<0 or y+j<0 or x+i>=len(map) or y+j >= len(map[0]):
                continue;
            if map[x+i][y+j] == '*':
                spaces_placed+=1
                map[x+i][y+j] = '.'
    return spaces_placed

def expand(map,x,y,nm):
    #print "---"
    #printMap(map)
    #raw_input()

    nm -= propagate(map,x,y)

    for i in range(-1,2):
        for j in range(-1,2):
            if i==j and i==0 or x+i<0 or y+j<0 or x+i>=len(map) or y+j >= len(map[0]):
                continue;
            minesFound = howManyMinesNearby(map,x+i,y+j)
            if minesFound <= nm and minesFound > 0 :
                if expand(copyMap(map),x+i,y+j,nm):
                    return True

            if nm == 0:
                printMap(map)
                return True
    return False

cases = int(raw_input())
inp = []


def iterateAndExpand(r,c,nm):
    if nm == 0:
        map = newMap()
        map[0][0] = 'c'
        printMap(map)
        return True

    for i in range(r):
        for j in range(c):
            map = newMap()
            map[i][j] = 'c'
            if expand(map,i,j,nm):
                return True

    return False
for i in range(cases):
    inp.append(raw_input().split(' '))

for n in range(cases):
    ret = ""
    r = int(inp[n][0])
    c = int(inp[n][1])
    m = int(inp[n][2])
    nm = r*c - m - 1 #not mines

    #sys.stdout.write("Processing " +str(r) + " " + str(c) + " " + str(m) + "\n")
    print "Case #" + str(n+1) + ":"

    if not iterateAndExpand(r,c,nm): print "Impossible"





