def check4(line, player):
    count = 0
    for i in xrange(4):
        if line[i] == player or line[i] == "T":
            count += 1
    return count == 4
   

f = open('A-large.in', 'r')
g = open('output.txt', 'w')

n = int(f.readline())
count = 1

while count <= n:
    matrix = [[""]*4, [""]*4,[""]*4,[""]*4]
    for i in xrange(4):    
        line = f.readline()
        if '\n' in line:
            line = line[:-1]
        line = list(line)

        for j in xrange(4):
            matrix[i][j] = line[j]
    
    xWin = False
    oWin = False
    for i in xrange(4):
        checkArray = matrix[i]
        xWin = xWin or check4(checkArray, "X")
        oWin = oWin or check4(checkArray, "O")
        
        checkArray = [matrix[j][i] for j in xrange(4)]
        xWin = xWin or check4(checkArray, "X")
        oWin = oWin or check4(checkArray, "O")
        
    checkArray = [matrix[i][i] for i in xrange(4)]
    xWin = xWin or check4(checkArray, "X")
    oWin = oWin or check4(checkArray, "O")
    
    checkArray = [matrix[i][3-i] for i in xrange(4)]
    xWin = xWin or check4(checkArray, "X")
    oWin = oWin or check4(checkArray, "O")
    
    full = True
    for i in xrange(4):
        for j in xrange(4):
            if matrix[i][j] == ".":
                full = False
    
    if xWin == oWin and not xWin and full:
        g.write("Case #" + str(count) + ": " + "Draw" + '\n')
    elif xWin and not oWin:
        g.write("Case #" + str(count) + ": " + "X won" + '\n')
    elif not xWin and oWin:
        g.write("Case #" + str(count) + ": " + "O won" + '\n')
    elif xWin == oWin and not xWin and not full:
        g.write("Case #" + str(count) + ": " + "Game has not completed" + '\n')
    else:
        g.write("Case #" + str(count) + ": " + "Error" + '\n')

    line = f.readline()
    count += 1
    
f.close()
g.close()