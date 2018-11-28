fin = file("B-large.in", "rU")
fout = file("B-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    grid = []

    line = fin.readline().strip().split()
    gridr = int(line[0])
    gridc = int(line[1])

    for r in xrange(gridr):
        line = fin.readline().strip().split()
        line2 = map(int, line)
        grid.append(line2)

    maxr = []
    maxc = []
    #compute max in each row
    for r in xrange(gridr):
        maxr.append(max(grid[r]))
    for c in xrange(gridc):
        tempmaxc = 0
        for r in xrange(gridr):
            tempmaxc = max(tempmaxc, grid[r][c])
        maxc.append(tempmaxc)

    #verify validity of grid - have row or column
    goodflag = 1
    for r in xrange(gridr):
        if goodflag == 0:
            break
        for c in xrange(gridc):
            if grid[r][c] < maxr[r] and grid[r][c] < maxc[c]:
                goodflag = 0
                break

    if goodflag:
        result = "YES"
    else:
        result = "NO"
   
    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
