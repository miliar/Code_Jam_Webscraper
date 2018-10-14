'''
Created on Sep 3, 2009

Question B

@author: AliJ
'''

def find_free(Basins):
    
    basinLabels = [chr(i+97) for i in range(26)]
    
    for i in range(len(Basins)):
        for j in range(len(Basins[i])):
            if Basins[i][j] not in basinLabels:
                return (i,j)
            
    return (-1,-1)

def sinkNeighbor(Grid, i, j, H, W):
    
    # Check the four neighbouring cells, in the right order.
    # North
    north = (i-1, j) if i-1 >= 0 else (i,j)
    west =  (i,j-1) if j-1 >=0 else (i,j)
    south = (i+1, j) if i+1 < H else (i,j)
    east = (i,j+1) if j+1 < W else (i,j)
    
    minAlt = min([Grid[y][x] for (y, x) in [north, west, south, east, (i,j)]])
    if minAlt == Grid[i][j]:
        return (i,j)
    elif minAlt == Grid[north[0]][north[1]]:
        return north
    elif minAlt == Grid[west[0]][west[1]]:
        return west
    elif minAlt == Grid[east[0]][east[1]]:
        return east
    else:
        return south
        
def findSink(Basin, i, j):
    
    next = Basin[i][j]
    
    while next != Basin[next[0]][next[1]]:
        next = Basin[next[0]][next[1]]
        #print next
    
    #print next
    return next

def process_case():
    
    # Idea: Completely handle sink a, then b, etc., until all cells are labelled.
    (Hstr, Wstr) = raw_input().split()
    (H, W) = (int(Hstr), int(Wstr))

    Grid = []
    Basins = [[-1 for i in range(W)] for j in range(H)]
    basinLabels = [chr(i+97) for i in range(26)]
    curLabel = 0
    
    for i in range(H):
        Grid.append([int(j) for j in raw_input().split()])
        
    for i in range(H):
        for j in range(W):
            Basins[i][j] = sinkNeighbor(Grid, i, j, H, W)
        
            
    for i in range(H):
        for j in range(W):
            Basins[i][j] = findSink(Basins, i, j)
            
            
    while(True):
        (nextI, nextJ) = find_free(Basins)
        if nextI == -1:
            break
        
        nextSink = Basins[nextI][nextJ]
        for i in range(H):
            for j in range(W):
                if Basins[i][j] == nextSink:
                    Basins[i][j] = basinLabels[curLabel]
                    
        curLabel += 1
        
    return Basins
            
            

numCases = int(raw_input())


for i in range(numCases):
            
    print "Case #"+str(i+1)+":"
    result = process_case()
    for row in result:
        for col in row:
            print col,
        print