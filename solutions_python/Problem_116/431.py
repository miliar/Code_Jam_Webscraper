fin = file("A-large.in", "rU")
fout = file("A-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    grid = []
    for j in xrange(4):
        #read grid
        line = fin.readline().strip()
        grid.append(line)
    line = fin.readline()

    emptyflag = 0
    wincase = 0 #1 for X, 2 for O

    #print grid
    #scan rows
    for r in xrange(4):
        cdict = {}
        for c in xrange(4):
            if grid[r][c] not in cdict:
                cdict[grid[r][c]] = 0
            cdict[grid[r][c]] += 1

        #checks
        if '.' in cdict:
            emptyflag = 1
        if 'X' in cdict and cdict['X'] == 4:
            wincase = 1
        if 'X' in cdict and cdict['X'] == 3 and 'T' in cdict:
            wincase = 1
        if 'O' in cdict and cdict['O'] == 4:
            wincase = 2
        if 'O' in cdict and cdict['O'] == 3 and 'T' in cdict:
            wincase = 2

    #scan columns
    for c in xrange(4):
        cdict = {}
        for r in xrange(4):
            if grid[r][c] not in cdict:
                cdict[grid[r][c]] = 0
            cdict[grid[r][c]] += 1

        #checks
        if '.' in cdict:
            emptyflag = 1
        if 'X' in cdict and cdict['X'] == 4:
            wincase = 1
        if 'X' in cdict and cdict['X'] == 3 and 'T' in cdict:
            wincase = 1
        if 'O' in cdict and cdict['O'] == 4:
            wincase = 2
        if 'O' in cdict and cdict['O'] == 3 and 'T' in cdict:
            wincase = 2

    #scan diagonals
    cdict = {}
    for d1 in xrange(4):
        if grid[d1][d1] not in cdict:
            cdict[grid[d1][d1]] = 0
        cdict[grid[d1][d1]] += 1
    if '.' in cdict:
        emptyflag = 1
    if 'X' in cdict and cdict['X'] == 4:
        wincase = 1
    if 'X' in cdict and cdict['X'] == 3 and 'T' in cdict:
        wincase = 1
    if 'O' in cdict and cdict['O'] == 4:
        wincase = 2
    if 'O' in cdict and cdict['O'] == 3 and 'T' in cdict:
        wincase = 2

    cdict = {}
    for d2 in xrange(4):
        if grid[d2][3-d2] not in cdict:
            cdict[grid[d2][3-d2]] = 0
        cdict[grid[d2][3-d2]] += 1
    if '.' in cdict:
        emptyflag = 1
    if 'X' in cdict and cdict['X'] == 4:
        wincase = 1
    if 'X' in cdict and cdict['X'] == 3 and 'T' in cdict:
        wincase = 1
    if 'O' in cdict and cdict['O'] == 4:
        wincase = 2
    if 'O' in cdict and cdict['O'] == 3 and 'T' in cdict:
        wincase = 2

    #output
    result = ""
    if wincase == 1:
        result = "X won"
    elif wincase == 2:
        result = "O won"
    elif wincase == 0 and emptyflag == 0:
        result = "Draw"
    elif wincase == 0 and emptyflag == 1:
        result = "Game has not completed"
    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
