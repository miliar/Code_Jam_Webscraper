import sys

def decodeTrip0(totpt):
    # totpt mod 3 = 0
    positive = lambda x: True if x >= 0 else False
    out = {'surp': None, 'nonsurp': None}
    i1 = (totpt / 3) - 1
    s = i1, i1+1, i1+2
    if all(map(positive, s)):
        out['surp'] = s
    i2 = totpt / 3
    ns = i2, i2, i2
    out['nonsurp'] = ns
    return out

def decodeTrip1(totpt):
    # totpt mod 3 = 1
    positive = lambda x: True if x >= 0 else False
    out = {'surp': None, 'nonsurp': None}
    i1 = (totpt - 4) / 3
    s = i1, i1+2, i1+2
    if all(map(positive, s)):
        out['surp'] = s
    i2 = (totpt - 1) / 3
    ns = i2, i2, i2+1
    if all(map(positive, ns)):
        out['nonsurp'] = ns
    return out

def decodeTrip2(totpt):
    # totpt mod 3 = 2
    positive = lambda x: True if x >= 0 else False
    out = {'surp': None, 'nonsurp': None}
    i1 = (totpt - 2) / 3
    s = i1, i1, i1+2
    if all(map(positive, s)):
        out['surp'] = s
    i2 = (totpt - 2) / 3
    ns = i1, i1+1, i1+1
    if all(map(positive, ns)):
        out['nonsurp'] = ns
    return out

def splitTriplets(totptsList):
    # input is the list of best scores
    tripsBoth = []
    tripsNonSurp = []
    tripsSurp = []
    negative = lambda x: True if x < 0 else False
    for totpt in totptsList:
        if totpt % 3 == 0:
            dec = decodeTrip0(totpt)
            if dec['surp'] is None:
                tripsNonSurp.append((totpt, dec))
            elif dec['nonsurp'] is None:
                tripsSurp.append((totpt, dec))
            else:
                tripsBoth.append((totpt, dec))
        elif totpt % 3 == 1:
            dec = decodeTrip1(totpt)
            if dec['surp'] is None:
                tripsNonSurp.append((totpt, dec))
            elif dec['nonsurp'] is None:
                tripsSurp.append((totpt, dec))
            else:
                tripsBoth.append((totpt, dec))
        elif totpt % 3 == 2:
            dec = decodeTrip2(totpt)
            if dec['surp'] is None:
                tripsNonSurp.append((totpt, dec))
            elif dec['nonsurp'] is None:
                tripsSurp.append((totpt, dec))
            else:
                tripsBoth.append((totpt, dec))
    return {'both': dict(enumerate(tripsBoth)),
            'onlySurp': tripsSurp,
            'onlyNonSurp': tripsNonSurp}

def choose_n(n, srcList):
    if n == 0:
        return [[]]
    else:
        out = []
        for cnt, elem in enumerate(srcList):
            out += map(lambda x: [elem] + x,
                       choose_n(n-1, srcList[:cnt] + srcList[(cnt+1):]))
        return out

def remDupes(listlist):
    out = []
    for li in listlist:
        li.sort()
        if not li in out:
            out.append(li)
    return out

def bestRes(triplet):
    return triplet[2]

def getHypoTrips(indices, maxIdx, tripDict):
    # indices mean "take the surp from that totalScore"
    outTrips = []
    sIndices = set(indices)
    for idx in range(maxIdx):
        if idx in sIndices:
            outTrips.append(tripDict['both'][idx][1]['surp'])
        else:
            outTrips.append(tripDict['both'][idx][1]['nonsurp'])
    outTrips += [topscore[1]['nonsurp']
                 for topscore in tripDict['onlyNonSurp']]
    outTrips += [topscore[1]['surp']
                 for topscore in tripDict['onlySurp']]
    # print 'outTrips:', outTrips
    return outTrips

def cntBestScrGTp(p, trips):
    # print 'trips', trips
    # print 'bres', map(bestRes, trips)
    return len([s for s in map(bestRes, trips) if s >= p])

def getMaxGoogGTp(p, nSurpTrips, totptsList):
    tripDict = splitTriplets(totptsList)
    # print 'tripDict', tripDict
    nSelect = nSurpTrips - len(tripDict['onlySurp'])
    indicesList = remDupes(choose_n(nSelect, range(len(tripDict['both']))))
    # print 'ilist', indicesList
    return max(map(lambda indices: \
                       cntBestScrGTp(p, getHypoTrips(indices,
                                                     len(tripDict['both']),
                                                     tripDict)),
                   indicesList))

infile = sys.argv[1]
infilh = open(infile)
infilh.readline()

outfile = open('out.txt', 'w')

for cnt, line in enumerate(infilh):
    line = line.rstrip().split()
    # print 'line', line
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    # print 'totalscores:', line[3:]
    result = getMaxGoogGTp(p, S, map(int, line[3:]))
    outfile.write('Case #' + str(cnt+1) + ': ' + str(result) + '\n')

outfile.close()
infilh.close()
