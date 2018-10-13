

def dotAverage(opponents, values):
    total = 0
    count = 0
    for (i, opp) in enumerate(opponents):
        if opp != None:
            count += 1
        if opp == 1:
            total += values[i]
    return float(total) / count

def getResultFromChar(ch):
    if ch == '0':
        return 0
    if ch == '1':
        return 1
    if ch == '.':
        return None
    raise "bad char " + ch

def readRow(l):
    return [getResultFromChar(ch) for ch in raw_input()[:l]]

def readTable():
    l = int(raw_input())
    res = []
    for i in range(l):
        res.append(readRow(l))
    return res

def getPlayedTable(table):
    return [[None if x == None else 1 for x in lst] for lst in table]

def getRPI(wp, owp, oowp):
    return 0.25 * wp + 0.5 * owp + 0.25 * oowp
    

def main():
    numCases = int(raw_input())
    for i in range(numCases):
        table = readTable()
        numTeams = len(table)
        played = getPlayedTable(table)
        wps = [dotAverage(table[j], table[j]) for j in range(numTeams)]
        owps = []
        for j in range(numTeams):
            adjustWps = []
            for k in range(numTeams):
                table2 = table[k][:]
                table2[j] = None
                adjustWps.append(dotAverage(table2, table2))
            owps.append(dotAverage(played[j], adjustWps))
        oowps = [dotAverage(played[j], owps) for j in range(numTeams)]
        rpis = [getRPI(wps[j], owps[j], oowps[j]) for j in range(numTeams)]
        print "Case #%d:" % (i + 1)
        for rpi in rpis:
            print rpi

main()
        
