def calcTrains(trains, T):
    nt = [0, 0]
    aval = [[], []]
    
    while len(trains) > 0:
        train = trains.pop(0)
        station = train[2]
        reuse = False
        if len(aval[station]) > 0:
            rt = aval[station][0]
            if rt <= train[0]:
                reuse = True
                aval[station].pop(0)

        if not reuse:
            nt[station] += 1
        
        aval[1-station].append(train[1] + T)
        aval[1-station].sort()
    
    return "%d %d" % (nt[0], nt[1])

def cTime(time, station):
    s, e = time.split()
    hs, ms = s.split(":")
    he, me = e.split(":")
    ms = int(hs) * 60 + int(ms)
    me = int(he) * 60 + int(me)
    return (ms, me, station)

fname = "B-large.in"
fin = open(fname, "r")
fOutName = fname.split(".")[0] + ".out"
fout = open(fOutName, "w")
num = int(fin.readline().strip("\n"))
for i in xrange(1, num + 1):
    T = int(fin.readline().strip("\n"))
    NA, NB = [int(x) for x in fin.readline().split()]
    trains = []
    for t in xrange(1, NA + 1):
        trains.append(cTime(fin.readline(), 0))
    for t in xrange(1, NB + 1):
        trains.append(cTime(fin.readline(), 1))
    trains.sort()
    #print trains
    str = "Case #%d: %s" % (i, calcTrains(trains, T))
    print str
    fout.write(str + "\n") 
fin.close()
fout.close()
