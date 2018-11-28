import sys

def getints():
    return [int(x) for x in sys.stdin.readline().strip().split()]
def getfloats():
    return [float(x) for x in sys.stdin.readline().strip().split()]


def fillgrid(nummines):
    lastrow = R - 1
    while nummines > 0:
        if nummines > C:
            grid[lastrow] = list('*' * C)
            nummines -= C
        else:
            grid[lastrow] = list('.' * (C - nummines) + '*' * nummines)
            nummines = 0
        lastrow -= 1

def printgrid():
    if swap:
        grid2 = [['.' for x in range(R)] for r in range(C)]
        #grid2 = ['.' * C] * R
        for r in range(R):
            for c in range(C):
                grid2[c][r] = grid[r][c]
        for row in grid2:
            print ''.join(row)
    else:
        for row in grid:
            print ''.join(row)


T = getints()[0]
for testcase in range(1,1+T):
    R,C,M = getints()
    print "Case #%d:" % (testcase)

    swap = False
    ok = False
    if C > R:
        R, C = C, R
        swap = True

    # C is smaller

    spaces = R*C - M

    grid = [['.' for x in range(C)] for r in range(R)]

    if spaces == 1:
        # easy
        fillgrid(M)
        ok = True
    elif C == 1:
        # easy
        fillgrid(M)
        ok = True
    elif C == 2:
        fillgrid(M)
        if spaces == 1:
            ok = True
        elif spaces == 2:
            ok = False
        else:
            ok = (spaces % 2) == 0
    else:
        # C >= 3

        def normalfill():
            #print spaces, C, M % C
            if M % C == C - 1:
                # one short of filling a row:
                # put one on the next row instead
                fillgrid(M - 1)
                grid[(spaces / C) - 1][C-1] = '*'
            else:
                fillgrid(M)


        if spaces >= 2 * C + 2:
            normalfill()
            #print "nromal"
            ok = True
        elif spaces <= 7 and (spaces % 2 == 1):
            ok = False
        elif 2 <= spaces <= 3:
            ok = False
        else:
            # spaces >= 4
            #print "dunno", spaces
            ok = True

            fillgrid(R*C-1)
            left = spaces - 4  # spaces left to place
            grid[0][1] = '.'
            grid[1][1] = '.'
            grid[1][0] = '.'

            if spaces % 2 == 1:
                left -= 1
                grid[2][2] = '.'


            #print " <<<<<<"
            #printgrid()
            #print ">>>>>"

            x = 2
            y = 2
            while left >= 2:
                #print 'a', left
                if left:
                    #print "Y"
                    left -= 2
                    grid[y][1] = '.'
                    grid[y][0] = '.'
                    y += 1
                #print 'b', left
                if left:
                    #print "X"
                    left -= 2
                    grid[0][x] = '.'
                    grid[1][x] = '.'
                    x += 1

            #Cprime = 3
            #fillgrid(M-1)
            #normalfill()
            #C = Cprime
            #ok = True
            #fillgrid(M - 1)
            #grid[(M / C)][C-1] = '*'
            #ok = True

            

    #if R*C - M < 2 * C + 1:
        # don't have a whole row clear

    if ok:
        grid[0][0] = 'c'
        printgrid()
    else:
        print "Impossible"
