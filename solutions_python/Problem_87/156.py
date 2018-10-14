fin = file("A-small-attempt2.in", "rU")
fout = file("A-small-attempt2.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip().split() #X S R t N
    length = int(line[0])
    walkspeed = int(line[1])
    runspeed = int(line[2])
    runtime = float(line[3])
    nwalkways = int(line[4])

    walkwaysa = []
    walkwaysb = []
    for j in xrange(nwalkways):
        line = fin.readline().strip().split() #Bi Ei wi
        wwbegin = int(line[0])
        wwend = int(line[1])
        wwspeed = int(line[2])

        walkwaysa.append([wwbegin, wwend])
        walkwaysb.append([wwspeed, wwbegin, wwend])
    walkwaysa.sort()
    walkwaysb.sort()

    #print walkwaysa
    #print walkwaysb

    totaltime = 0.0

    #run on non-walkways first

    #print 'nonwalkway'
    #calculate non-walkway time
    currpoint = 0
    for wwbegin, wwend in walkwaysa:
        #print 'this', wwbegin, wwend, currpoint
        if currpoint == wwbegin:
            currpoint = wwend
            continue
        if runtime > 0:
            t = (float)(wwbegin-currpoint)/(runspeed)
            if t > runtime:
                drun = runspeed*runtime
                dwalk = wwbegin-currpoint-drun
                t = runtime + (float)(dwalk)/walkspeed
            totaltime += t
            runtime -= t
        else: #walk
            t = (float)(wwbegin-currpoint)/(walkspeed)
        currpoint = wwend
        #print currpoint, wwbegin, totaltime

    if length - currpoint > 0:
        if runtime > 0:
            t = (float)(length-currpoint)/(runspeed)
            if t > runtime:
                drun = runspeed*runtime
                dwalk = length-currpoint-drun
                t = runtime + (float)(dwalk)/(walkspeed)
            totaltime += t
            runtime -= t
        else:
            totaltime += (float)(length-currpoint)/(walkspeed)
        #print currpoint, length, totaltime

    #print ''
    #print 'walkway'

    #calculate runnable time on walkways
    for wwspeed, wwbegin, wwend in walkwaysb:
        #if runspeed-walkspeed > wwspeed+runspeed and :
        if runtime > 0:
            t = (float)(wwend-wwbegin)/(wwspeed+runspeed) #time if running
            if t > runtime: #can't run for that long
                drun = (wwspeed+runspeed)*runtime #d = s*t
                dwalk = wwend-wwbegin-drun #distance walked
                t = runtime + (float)(dwalk)/(wwspeed+walkspeed)
            totaltime += t
            runtime -= t
        else: #walk
            t = (float)(wwend-wwbegin)/(wwspeed+walkspeed)
            totaltime += t
        #print wwbegin, wwend, totaltime
    
    strout = "Case #" + str(i+1) + ": " + str(totaltime) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
