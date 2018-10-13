import sys

def getnext(gen, type):
    try:
        l = gen.next().strip("\n")
        return type(l)
    except StopIteration:
        return None

def minutes(time):
    h, m = [int(i) for i in time.split(":")]
    return h*60 + m

def splitTT(timetable):
    return [minutes(t) for t in timetable.split(" ")]

def matchTrains(aT, bT, delay):
    matchedA = [0]*len(aT)
    matchedB = [0]*len(bT)
    #Match A Trains
    for i in range(len(aT)):
        for j in range(len(bT)):
            if (aT[i][1] + delay <= bT[j][0]) and not matchedB[j]:
                matchedB[j] = 1
                break
    #Match B Trains
    for i in range(len(bT)):
        for j in range(len(aT)):
            if (bT[i][1] + delay <= aT[j][0]) and not matchedA[j]:
                matchedA[j] = 1
                break
    return str(matchedA.count(0)) + " " + str(matchedB.count(0))
                

if __name__ == "__main__":
    infi = sys.argv[1]
    reader = open(infi,'r').xreadlines()
    output = open(sys.argv[0]+'-output', 'w')
    N = getnext(reader, int)
    for n in range(N):
        T = getnext(reader, int)
        NA, NB = [int(i) for i in getnext(reader, str).split(" ")]
        a_trains = [splitTT(getnext(reader, str)) for a in range(NA)]
        b_trains = [splitTT(getnext(reader, str)) for b in range(NB)]
        a_trains.sort()
        b_trains.sort()
        output.write("Case #%d: %s\n" % (n+1, matchTrains(a_trains, b_trains,T)))
