outfile = open("outputA.txt", "w")
linenum = 0
case = 1
stat = "teams"
for line in open("A-large.in", "rU"):
    if linenum != 0:
        if stat == "teams":
            teamnum = int(line.strip())
            teamlist = []
            teams = 0
            stat = "sort"
        elif stat == "sort":
            teamlist.append(list(line.strip()))
            teams += 1
            if teams == teamnum:
                outfile.write("Case #" + str(case) + ":\n")
                case += 1
                stat = "teams"
                #print teamlist
                WPlist = []
                for team in teamlist:
                    WPlist.append([float(team.count('1')),float(team.count('0') + team.count('1'))])
                #print WPlist
                OWPlist = []
                for team1 in xrange(0, len(WPlist)):
                    OWP1 = 0
                    counter = 0
                    for team2 in xrange(0, len(WPlist)):
                        if team1 != team2:
                            if teamlist[team2][team1] == '0':
                                OWP1 += float(WPlist[team2][0])/float(WPlist[team2][1] - 1)
                                counter += 1
                            elif teamlist[team2][team1] == '1':
                                OWP1 += float(WPlist[team2][0] - 1)/float(WPlist[team2][1] - 1)
                                counter += 1
                    OWPlist.append(float(OWP1)/counter)
                #print OWPlist
                OOWPlist = []
                for team1 in xrange(0, len(OWPlist)):
                    OWPtotal = 0
                    counter = 0
                    for team2 in xrange(0, len(OWPlist)):
                        if team1 != team2 and teamlist[team2][team1] != ".":
                            OWPtotal += OWPlist[team2]
                            counter += 1
                    OOWPlist.append(float(OWPtotal)/counter)
                #print OOWPlist
                for index in xrange(0, len(WPlist)):
                    score = 0.25 * float(WPlist[index][0])/float(WPlist[index][1]) + 0.5 * OWPlist[index] + 0.25 * OOWPlist[index]
                    outfile.write(str(score) + "\n")                       
                    
                
    linenum += 1
    
outfile.close()
