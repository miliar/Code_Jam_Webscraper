f = open("A-large (2).in")
first, matchCount = True, -1
matchData = []

def scoreMatch(matchData):
    wpData = []
    for m in matchData:
        wpData.append([int(s) for s in m if s != "."])
    wps = [sum(m) / float(len(m)) for m in wpData] 

    owps = []
    for team, m in enumerate(matchData):
        opWPs = []
        for opp, win in enumerate(m):
            if win == "0" or win == "1":
                # opp is index of opponent
                # throw out "."'s and the game against team
                oppData = matchData[opp][0:team] + matchData[opp][team+1:]
                cleanOppData = [int(s) for s in oppData if s != "."]
                opWPs.append(sum(cleanOppData) / float(len(cleanOppData)))
        owps.append(sum(opWPs) / float(len(opWPs)))

    oowps = []
    for team, m in enumerate(matchData):
        ooWPs = []
        for opp, win in enumerate(m):
            if win == "0" or win == "1":
                ooWPs.append(owps[opp])
        oowps.append(sum(ooWPs) / float(len(ooWPs)))

    res = [(0.25 * wp) + (0.50 * owp) + (0.25 * oowp) for wp, owp, oowp in zip(wps, owps, oowps)]
    return res

case = 1
for line in f:
    if first:
        first=False
        continue
    if matchCount <= 0:
        if len(matchData) > 0:
            print "Case #%d:" % case
            res = scoreMatch(matchData)
            for rpi in res:
                print rpi
            case += 1
        matchCount = int(line.strip())
        matchData = []
    else:
        matchData.append(list(line.strip()))
        matchCount -= 1

f.close()

if len(matchData) > 0:
    print "Case #%d:" % case
    res = scoreMatch(matchData)
    for rpi in res:
        print rpi
    case += 1
