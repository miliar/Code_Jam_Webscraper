f = open("A-small-attempt0.in", 'rU')
w = open("A-small.out", 'w')

def checkDiagonal(g):
    pass

def checkHorizontal(g):
    pass
def checkVertical(g):
    pass
def checkInProgress(g):
    pass
def checkDraw(g):
    pass

#read the first line to get the number of cases in the file
numCases = int(f.readline())

for n in range(0,numCases):
    game = []
    win = False
    #win
    for o in range(4):
        line = f.readline()
        game.append(line.strip())
    f.readline() #kill the separating line
    #print game
    #checkDiagonal
    x = 3
    diag1 = []
    diag2 = []
    for o in range(4):
        diag1.append(game[o][o])
        diag2.append(game[o][x])
        x-=1
    if diag1.count('O') == 4 or diag2.count('O') == 4:
        win = "O won"

    elif diag1.count('O') == 3 or diag2.count('O') == 3:
        if diag1.count('T') == 1 or diag2.count('T') == 1:
            win = "O won"
            
    elif diag1.count('X') == 4 or diag2.count('X') == 4:
        win = "X won"
        
    elif diag1.count('X') == 3 or diag2.count('X') == 3:
        if diag1.count('T') == 1 or diag1.count('T') == 1:
            win = "X won"

    #checkVertical
    if win == False:
        for o in range(4):
            vert = []
            for x in range(4):
                vert.append(game[x][o])
            #check vert
            if vert.count('O') == 4:
                win = "O won"
                break
            elif vert.count('X') == 4:
                win = "X won"
                break
            elif vert.count('O') == 3:
                if vert.count('T') == 1:
                    win = "O won"
                    break
            elif vert.count('X') == 3:
                if vert.count('T') == 1:
                    win = "X won"
                    break
     #checkHorizontal
    if win == False:
        for o in range(4):
            if game[o].count('O') == 4:
                win = "O won"
                break
            elif game[o].count('X') == 4:
                win = "X won"
                break
            elif game[o].count('O') == 3:
                if game[o].count('T') == 1:
                    win = "O won"
                    break
            elif game[o].count('X') == 3:
                if game[o].count('T') == 1:
                    win = "X won"
                    break
    if win == False:
         
        #check for draw/in progress
        dots = []
        for o in range(4):
            if '.' in game[o]:
                dots.append('.')
        if len(dots) == 0:
            win = "Draw"
        else:
            win = "Game has not completed"
    w.write("Case #%d: %s\n" % (n+1, win))
    print "Case #%d: %s\n" % (n+1, win)
        
w.close()
f.close()
    
    
