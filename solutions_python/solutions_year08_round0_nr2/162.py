def findMinTrains(arrivals,departures):
    starting = 0
    cur = 0
    arrivals.sort()
    departures.sort()
    
    for departure in departures:
        while len(arrivals)>0 and arrivals[0] <= departure:
            cur += 1
            arrivals = arrivals[1:]
        if not cur:
            starting += 1
            cur += 1
        cur -= 1
    
    return starting

def getMinutes(instr):
    instr = instr.split(":")
    if instr[0][0] == 0: instr[0][0] = instr[0][1]
    if instr[1][0] == 0: instr[1][0] = instr[1][1]
    return int(instr[1]) + 60 * int(instr[0])

n = int(raw_input())
for i in xrange(n):
    turnaround = int(raw_input())
    m,p = (int(x) for x in raw_input().split())
    Adepartures = []
    Bdepartures = []
    Aarrivals = []
    Barrivals = []
    for j in xrange(m):
        route = raw_input().split()
        Adepartures.append(getMinutes(route[0]))
        Barrivals.append(getMinutes(route[1])+turnaround)
    for j in xrange(p):
        route = raw_input().split()
        Bdepartures.append(getMinutes(route[0]))
        Aarrivals.append(getMinutes(route[1])+turnaround)
    print "Case #%d: %d %d" % (i+1,findMinTrains(Aarrivals,Adepartures),findMinTrains(Barrivals,Bdepartures))
