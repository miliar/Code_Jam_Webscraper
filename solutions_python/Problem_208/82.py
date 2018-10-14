f = open('C:\\Users\\djspence\\Downloads\\C-small-attempt0.in', 'r')

tries = int(f.readline())

#only doing small right now

for case in range(0, tries):
    vals0 = f.readline().strip().split(' ')
    n = int(vals0[0])
    horses = []
    for i in range(0, n):
        curVals = f.readline().strip().split()
        horses.append([int(curVals[0]), int(curVals[1])])
    getToNext = []
    for i in range(0, n - 1):
        curVals = f.readline().strip().split(' ')
        getToNext.append(int(curVals[i + 1]))
    f.readline() #last city
    f.readline() #take care of the Q=1 line
    
    triples = [set() for i in range(0, n)]
    triples[0].add((0, horses[0][0], horses[0][1])) #time elapsed, horse distance left, horse speed
    
    for i in range(0, n - 1):
        dist = getToNext[i]
        for trip in triples[i]:
            if dist <= trip[1]:
                triples[i + 1].add((trip[0]+dist*1.0/trip[2], trip[1]-dist, trip[2]))
                triples[i + 1].add((trip[0]+dist*1.0/trip[2], horses[i+1][0], horses[i+1][1]))
        toRemove = []
        for trip1 in triples[i + 1]:
            for trip2 in triples[i + 1]:
                if trip1 == trip2:
                    continue
                if trip1[0] <= trip2[0] and trip1[1] >= trip2[1] and trip1[2] >= trip2[2]:
                    toRemove.append(trip2)
        for removing in toRemove:
            if removing in triples[i + 1]:
                triples[i + 1].remove(removing)
    times = []
    for trip in triples[n - 1]:
        times.append(trip[0])
    print("Case #" + str(case+1)+": " + str(min(times)))