def testRow(r):
    Xs = 0
    Os = 0
    Ts = 0
    Ds = 0
    for ch in r:
        if ch=='X':
            Xs+=1
        elif ch=='O':
            Os+=1
        elif ch=='.':
            Ds+=1
        elif ch=='T':
            Ts+=1
        else:
            print "unknown char: " + ch
    if Xs==4:
        return 'X'
    if Xs==3 and Ts==1:
        return 'X'
    if Os==4:
        return 'O'
    if Os==3 and Ts==1:
        return 'O'      
    if Ds==0:
        return 'D' #draw potential
    return 'N' #defs not a draw

def testBoard(b):
    drawPot = True
    for i in range(0,4): #test horizontals
        l = []
        for j in range(0,4):
            l.append(b[i][j])
        a = testRow(l)
        if a=='X':
            return "X won"
        elif a=='O':
            return 'O won'
        elif a=='N':
            drawPot = False
    for i in range(0,4): #test verticals
        l = []
        for j in range(0,4):
            l.append(b[j][i])
        a = testRow(l)
        if a=='X':
            return "X won"
        elif a=='O':
            return 'O won'
        elif a=='N':
            drawPot = False
        l = []
        for i in range(0,4):
            l.append(b[i][i])
        a = testRow(l)
        if a=='X':
            return "X won"
        elif a=='O':
            return 'O won'
        elif a=='N':
            drawPot = False
        l = []
        for i in range(0,4):
            l.append(b[i][3-i])
        a = testRow(l)
        if a=='X':
            return "X won"
        elif a=='O':
            return 'O won'
        elif a=='N':
            drawPot = False
        if drawPot:
            return "Draw"
        return "Game has not completed"
with open('input.txt') as f:
    lines = f.readlines()
        
tcases = int(lines[0])

for case in range(0,tcases):
    brd = []
    baseRow = case*5 + 1
    for i in range(0,4):
        brd.append(lines[baseRow+i])
    print "Case #" + str(case+1) + ": " + testBoard(brd)
    



