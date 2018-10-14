#Tested locally with Python 2.6.2 on OS X 10.6.0
#Oops. x is actually up and down and y is left and right. Fail = me.
def search(x, y, H, W, bas, heights, maxBas):
    lowestNeighbor = heights[x][y]
    lowestDir = 0 #1 is N, 2 is W, 3 is E, 4 is S, 0 is none
    if x>0 and heights[x-1][y] < lowestNeighbor:
        lowestNeighbor = heights[x-1][y]
        lowestDir = 1
    if y>0 and heights[x][y-1] < lowestNeighbor:
        lowestNeighbor = heights[x][y-1]
        lowestDir = 2
    if y<W-1 and heights[x][y+1] < lowestNeighbor:
        lowestNeighbor = heights[x][y+1]
        lowestDir = 3
    if x<H-1 and heights[x+1][y] < lowestNeighbor:
        lowestNeighbor = heights[x+1][y]
        lowestDir = 4

    ret = 0
    if lowestDir is 0:
        if bas[x][y] is 0:
            maxBas+=1
            bas[x][y] = maxBas
            return [maxBas,maxBas]
        else:
            return [bas[x][y],maxBas]
    elif lowestDir is 1:
        ret = search(x-1,y,H,W,bas,heights,maxBas)
        bas[x][y] = ret[0]
        maxBas = ret[1]
        return [ret[0],maxBas]
    elif lowestDir is 2:
        ret = search(x,y-1,H,W,bas,heights,maxBas)
        bas[x][y] = ret[0]
        maxBas = ret[1]
        return [ret[0],maxBas]
    elif lowestDir is 3:
        ret = search(x,y+1,H,W,bas,heights,maxBas)
        bas[x][y] = ret[0]
        maxBas = ret[1]
        return [ret[0],maxBas]
    elif lowestDir is 4:
        ret = search(x+1,y,H,W,bas,heights,maxBas)
        bas[x][y] = ret[0]
        maxBas = ret[1]
        return [ret[0],maxBas]
    

input = open('B-large.in','r')
output = open('B-large.out','w')
T = int(input.next())

for quoi in range(0,T):
    H,W = input.next().split(' ')
    H = int(H)
    W = int(W)
    maxBas = 0

    basins = [[0 for j in range(0,W)] for i in range(0,H)]
    map = []

    for i in range(0,H):
        map.append([])
        for j in input.next().split(' '):
            map[i].append(int(j))
    
    for i in range(0,H):
        for j in range(0,W):
            if basins[i][j] == 0:
                maxBas = search(i,j,H,W,basins,map,maxBas)[1]

    output.write("Case #"+str(quoi+1)+":\n")
    for i in range(0,H):
        line = ""
        for j in range(0,W):
            line+=chr(basins[i][j]+96)
            if j != W-1:
                line+=" "
            else:
                line+="\n"
                output.write(line)
