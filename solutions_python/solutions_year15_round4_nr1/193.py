
directions = ['^', '<', '>', 'v'] 
def nastepnik(p, grid):
    r, c, arrowy = p
        
def calcColumn(grid, row, column):
    columnList = []
    for r in range(row):
        s = 0
        for c in range(column):
            if grid[r][c] in directions:
                s+=1
        columnList.append(s)
    return columnList
            
def calcRow(grid, row, column):
    columnList = []
    for c in range(column):
        s = 0
        for r in range(row):
            if grid[r][c] in directions:
                s+=1
        columnList.append(s)
    return columnList



def hasNext(p, grid, column, row):
    posR, posC, direction = p
    posR_first = posR
    posC_first = posC
    if direction == '^':
        while posR >= 0:
            posR -= 1
            if grid[posR][posC] in directions:  
                return True
        return False
    if direction == 'v':
        while posR < row:
            posR += 1
            if grid[posR][posC] in directions:
                return True
        return False
    if direction == '<':
        while posC >= 0:
            posC -= 1
            if grid[posR][posC] in directions:
                return True
        return False
    if direction == '>':
        while posC < column:
            posC += 1
            if grid[posR][posC] in directions:
                return True
        return False
    
     

T = int(raw_input())
for t in range(T):
    points = []
    row, column = map(int, raw_input().split(' '))
    grid = [[0 for x in range(120)] for x in range(120)] 
    for r in range(row):
        rowString = raw_input()
        for c, elt in enumerate(rowString):
            if elt in directions:
                points.append((r, c, elt))
            grid[r][c] = elt
    for r in range(row):
        output = ""
        for c in range(column):
            output += grid[r][c]
    ile = 0
    for p in points:
        if not hasNext(p, grid, column, row):
            ile+=1
    rowIle = calcColumn(grid, row, column)
    colIle =  calcRow(grid, row, column)
    zle = False 

    for r in range(row):
        for c in range(column):
            if grid[r][c] in directions and rowIle[r] == 1 and colIle[c] == 1:
                zle = True
        
    if zle: 
        print "Case #%d: %s"  % (t+1, "IMPOSSIBLE")
    else:
        print "Case #%d: %d" % (t+1, ile)
