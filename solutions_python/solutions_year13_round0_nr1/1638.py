def check(F):
    #print F
    #Check horizontals
    for i in range(4):
        xwin = True
        owin = True
        for j in range(4):
            if not (F[i][j] == 'X' or F[i][j] == 'T'):
                xwin = False

            if not (F[i][j] == 'O' or F[i][j] == 'T'):
                owin = False

        if xwin:
            print "X won"
            return
        if owin:
            print "O won"
            return

    #Check verticals
    for i in range(4):
        xwin = True
        owin = True
        for j in range(4):
            if not (F[j][i] == 'X' or F[j][i] == 'T'):
                xwin = False

            if not (F[j][i] == 'O' or F[j][i] == 'T'):
                owin = False

        if xwin:
            print "X won"
            return
        if owin:
            print "O won"
            return

    #Check right-down
    xwin = True
    owin = True
    for i in range(4):
        if not (F[i][i] == 'X' or F[i][i] == 'T'):
            xwin = False

        if not (F[i][i] == 'O' or F[i][i] == 'T'):
            owin = False
        
    if xwin:
        print "X won"
        return
    if owin:
        print "O won"
        return

    #Check right-down
    xwin = True
    owin = True
    for i in range(4):
        if not (F[3 - i][i] == 'X' or F[3 - i][i] == 'T'):
            xwin = False

        if not (F[3 - i][i] == 'O' or F[3 - i][i] == 'T'):
            owin = False
        
    if xwin:
        print "X won"
        return
    if owin:
        print "O won"
        return

    #Check verticals
    for i in range(4):
        for j in range(4):
            if F[i][j] == '.':
                print "Game has not completed"
                return

    print "Draw"

f = open('A-large.in')
T = int(f.readline().strip())

for i in range(T):
    F = []
    for a in range(4):
        F.append(f.readline().strip())
    f.readline()
    print "Case #" + str(i + 1) + ":",
    check(F)