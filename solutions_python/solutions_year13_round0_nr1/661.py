import time

def Check(grid,x,xIn,y,yIn,last):
    if x == 4 or y == 4:
        return last
    v = grid[x][y]
    if v != '.' and (last == 'NA' or v == 'T' or last == 'T' or v == last):
        return Check ( grid, x + xIn, xIn, y + yIn, yIn, last if v == 'T' else v )
    return False
t = time.clock()
f = open("ProblemA-Large.txt")
f.readline()

outFile = open("ProblemA-Out.txt",'w')
c = 0
while True:
    c+=1
    grid = []
    for i in range(4):
        grid.append(f.readline()[:-1])
    print grid
    if len(grid[0]) == 0:
        break
    final = ""
    for i in range(4):
        final = Check(grid,0,1,i,0,'NA')
        if not final:
            final = Check(grid,i,0,0,1,'NA')
            if final:
                break
        else:
            break
    if not final:
        final = Check(grid,0,1,0,1,'NA')
        if not final:
            final = Check(grid,3,-1,0,1,'NA')
    message = ""
    if final:
        message = final + " won"
    else:
        draw = True
        for i in grid:
            if '.' in i:
                draw = False
                break
        message = "Draw" if draw else "Game has not completed"
    outFile.write("Case #{0}: {1}\n".format(c, message))
    print "Case #{0}: {1}".format(c, message)
    
    if len(f.readline()) == 0:
        break
print time.clock() - t
f.close()
outFile.close()
