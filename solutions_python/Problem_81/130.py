fin = file("A-large.in", "rU")
fout = file("A-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    nteams = int(fin.readline().strip())
    grid = []
    for j in xrange(nteams):
        grid.append(fin.readline().strip())

    winper = []
    #calculate WP
    for teamgames in grid:
        nwin = 0
        ntotal = 0
        for game in teamgames:
            if game == '0':
                ntotal += 1
            elif game == '1':
                nwin += 1
                ntotal += 1
        winper.append((nwin, ntotal))

    #print wins

    owin = []
    owptotalsum = 0.0
    #calculate OWP (count wins against other team)
    for j in xrange(nteams): #each team
        owpsum = 0.0 #sum of percentages
        teamcount = 0
        for k in xrange(nteams):
            if k == j or grid[k][j] == '.':
                continue
            teamcount += 1
            winval = winper[k][0]
            totalval = winper[k][1]
            if grid[k][j] == '0': #remove game
                totalval -= 1
            elif grid[k][j] == '1':
                winval -= 1
                totalval -= 1
            owpsum += float(winval)/float(totalval)
        owpsum = float(owpsum)/float(teamcount)
        owptotalsum += owpsum
        owin.append(owpsum)

    oowin = []
    #calculate OOWP (count wins against other team)
    for j in xrange(nteams): #each team
        oowpsum = 0.0 #sum of percentages
        teamcount = 0
        for k in xrange(nteams):
            if k == j or grid[k][j] == '.':
                continue
            teamcount += 1
            oowpsum += owin[k]
        oowpsum = oowpsum/teamcount
        oowin.append(oowpsum)

    strout = "Case #" + str(i+1) + ":\n"
    for j in xrange(nteams):
        result = 0.25 * (float(winper[j][0])/float(winper[j][1])) + 0.50 * owin[j] + 0.25 * oowin[j]
        
        strout += str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
