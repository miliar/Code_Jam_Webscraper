def main():
    #caseSize = 1
    f = open('input.txt','r')
    lines = f.readlines()
    lines = map(lambda x: x.rstrip("\n"), lines)
    f.close()
    count = int(readNLines(1,lines)[0])
    output = ""
    for cNum in range(count):
        nTeams = int(readNLines(1,lines)[0])
        case = readNLines(nTeams,lines)
        results = calcGameRes(case)
        res = calcRPIs(results,nTeams)
        output+= "Case #%d: %s\n" % (cNum+1,res)
    f = open('output.txt','w')
    f.write(output)
    f.close()
    print output

def calcGameRes(rows):
    output = {}
    i = 0
    for row in rows:
        j = 0
        for game in row:
            if i!=j:
                if game != ".":
                    output["%d%d"%(i,j)] = int(game)
            j+=1
        i += 1
    return output
            
def calcRPIs(results,nTeams):
    wps = {}
    owps = {}
    oowps = {}
    for cTeam in range(nTeams):
        wp = calcWP(results,nTeams,cTeam)
        wps[cTeam] = wp
        #print wp
    for cTeam in range(nTeams):
        total = 0.0
        owpTot = 0.0
        #print "CTEAM: %d" % cTeam
        for them in range(nTeams):
            if cTeam!=them and "%d%d"%(cTeam,them) in results:
                owpi = calcOWP(results,nTeams, cTeam, them)
                #print "OWPI " + str(owpi)
                total += 1
                owpTot += owpi
        owp = float(owpTot)/float(total)
        #print "OWP:%f"%owp
        owps[cTeam]=owp
    for cTeam in range(nTeams):
        total = 0.0
        oowpTotal = 0.0
        for them in range(nTeams):
            if cTeam!=them and "%d%d"%(cTeam,them) in results:
                oowpTotal+=owps[them]
                total += 1
        oowp = float(oowpTotal)/float(total)
        oowps[cTeam]=oowp
        #print "OOWP " + str(oowp)
    output = ""
    for cTeam in range(nTeams):
        myRpi = .25*wps[cTeam]+.5*owps[cTeam]+.25*oowps[cTeam]
        #print "%d: %f"%(cTeam,myRpi)
        output += "\n%.12f"%myRpi
    return output
        
def calcWP(results,nTeams,i):
    tot = 0
    wins = 0
    for j in range(nTeams):
        key = "%d%d"%(i,j)
        if key in results.keys():
            tot += 1
            wins += results[key]
    return float(wins)/float(tot)

def calcOWP(results,nTeams,me,them):
    newRes = {x:results[x] for x in results.keys() if str(me) not in x}
    return calcWP(newRes,nTeams,them)

def readNLines(num, lines):
    toReturn = lines[0:num]
    del lines[0:num]
    lines = lines[num:]
    return toReturn

if __name__=="__main__":
    main()
