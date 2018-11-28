from decimal import *
getcontext().prec = 20

fin = open("A-large.in")
fout = open("A-large.out", "wt")

numCases = int(fin.readline().strip())

def output(string):
    print string
    fout.write(string)
    
for caseIndex in range(1,numCases+1):
    output("Case #%d:\n" % caseIndex)

    numTeams = int(fin.readline().strip())
    matches = [[]]*numTeams
    wps = [0.0] * numTeams
    wincounts = [0]*numTeams
    matchcounts = [0]*numTeams
    owps = [0.0]*numTeams
    opponents = [[]]*numTeams
    for teamNo1 in range(0,numTeams):
        matches[teamNo1] = fin.readline().strip()
        #print "Team %d: Matches: %s" %  (teamNo1,matches[teamNo1])
        teamNo2 = 0
        opponents[teamNo1] = []
        for match in matches[teamNo1]: 
            if match!='.':
                matchcounts[teamNo1]+=1
                opponents[teamNo1].append(teamNo2)
            if match=='1':
                wincounts[teamNo1]+=1

            teamNo2+=1
            
        if matchcounts[teamNo1]>0:
            wps[teamNo1] = 100.0*float(wincounts[teamNo1])/float(matchcounts[teamNo1])
        #print "WP %d: %f, opponents: %s" % (teamNo1, wps[teamNo1], ",".join(map(str, opponents[teamNo1])))

    # calculate owp from wps
    for teamNo1 in range(0,numTeams):
        allWinsWithoutMe = 0
        allMatchesWithoutMe = 0
        wpsWithoutMe = [0.0] * numTeams
        sumwpsWithoutMe = 0.0
        #for teamNo2 in range(0,numTeams):
        for teamNo2 in opponents[teamNo1]:
            if teamNo1==teamNo2:
                continue
            winsWithoutMe = wincounts[teamNo2]
            matchesWithoutMe = matchcounts[teamNo2]
            winAgainstMe = matches[teamNo2][teamNo1]
            
            if winAgainstMe=='.':
                continue
            if winAgainstMe=='1':
                winsWithoutMe-=1
                matchesWithoutMe-=1
            else:
                if winAgainstMe=='0':
                    matchesWithoutMe-=1
            #allWinsWithoutMe += winsWithoutMe
            #allMatchesWithoutMe += matchesWithoutMe
            if matchesWithoutMe>0:
                wpsWithoutMe[teamNo1] = 100*float(winsWithoutMe)/float(matchesWithoutMe)
                sumwpsWithoutMe += wpsWithoutMe[teamNo1]
        if len(opponents[teamNo1])>0:
            owps[teamNo1] = sumwpsWithoutMe/float(len(opponents[teamNo1]))
        #if allMatchesWithoutMe>0:
        #    owps[teamNo1] = 100.0*float(allWinsWithoutMe)/float(allMatchesWithoutMe)

        #print "OWP %d: %f" % (teamNo1,owps[teamNo1])

    
    # oowps
    oowps = [0.0] * numTeams
    rpis = [0.0] * numTeams
    for teamNo1 in range(0,numTeams):
        sumowp = 0.0
        for teamNo2 in opponents[teamNo1]:#(0,numTeams):
            if teamNo1==teamNo2:
                continue
            sumowp+=owps[teamNo2]
        if len(opponents[teamNo1])>0:
            oowps[teamNo1] = float(sumowp)/float(len(opponents[teamNo1]))
        #print "WP   %d: %f" % (teamNo1, wps[teamNo1])
        #print "OWP  %d: %f" % (teamNo1, owps[teamNo1])
        #print "OOWP %d: %f" % (teamNo1, oowps[teamNo1])
        rpis[teamNo1] = 0.25*wps[teamNo1] + 0.50*owps[teamNo1] + 0.25*oowps[teamNo1]
        #print "RPI %d: %0.12f" % (teamNo1, rpis[teamNo1])
            
        output("%0.9f\n" % (rpis[teamNo1]*0.01))

fin.close()
fout.close()

        
