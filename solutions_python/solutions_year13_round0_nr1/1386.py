def check(string,char):
    for s in string:
        if s != char and s != "T":
            return False
    return True

def win(grid,char):
    if check(grid[0],char) or check(grid[1],char) or check(grid[2],char) or check(grid[3],char):
        return True
    
    for i in xrange(4):
        col = ""
        for j in xrange(4):
            col += grid[j][i]
        if check(col,char):
            return True
    
    return check(grid[0][0]+grid[1][1]+grid[2][2]+grid[3][3],char) or check(grid[3][0]+grid[2][1]+grid[1][2]+grid[0][3],char)
    

out = open("P1.out","w")
data = open("P1_large.txt")
cases = int(data.readline())
for case in xrange(cases):
    grid = []
    for _ in xrange(4):
        grid.append(data.readline().strip())
        
    out.write("Case #%i: " %(case+1))
    if win(grid,"X"):
        out.write("X won\n")
    elif win(grid,"O"):
        out.write("O won\n")
    else:
        if '.' in grid[0]+grid[1]+grid[2]+grid[3]:
            out.write("Game has not completed\n")
        else:
            out.write("Draw\n")
    data.readline()