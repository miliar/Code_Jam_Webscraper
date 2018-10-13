def add_T(time, t):
    hr = int(time[:2])
    min = int(time[3:])
    if t < (60-min):
        min += t
    else:
        hr += 1
        min = t - (60-min)
    return '%s:%s' % (str(hr).zfill(2), str(min).zfill(2))

def isNotAvail(avail, depart):
    toRtn = True
    avail.sort()
    for t in avail:
        if t <= depart:
            avail.remove(t)
            toRtn = False
            break
    return toRtn


f = open('B-small-attempt3.in')
output = open('B-small.out', 'w')

N = int(f.readline())
for n in range(1,N+1):
    T = int(f.readline())
    nextLn = f.readline().split()
    NA = int(nextLn[0])
    NB = int(nextLn[1])
    fromA = dict()
    for a in range(0,NA):
        schdl = f.readline().split()
        if schdl[0] in fromA:
            fromA[schdl[0]].append(schdl[1])
            fromA[schdl[0]].sort()
        else:
            fromA[schdl[0]] = [schdl[1]]
    fromB = dict()
    for b in range(0,NB):
        schdl = f.readline().split()
        if schdl[0] in fromB:
            fromB[schdl[0]].append(schdl[1])
            fromB[schdl[0]].sort()
        else:
            fromB[schdl[0]] = [schdl[1]]
    output.write('Case #%u: ' % n)
    departA = fromA.keys()
    departA.sort()
    departB = fromB.keys()
    departB.sort()
    
    trainsA = 0
    trainsB = 0
    availA = []
    availB = []
    while len(departA) > 0 and len(departB) > 0:
        a = departA[0]
        b = departB[0]
        if a < b:
            if len(availA) == 0 or isNotAvail(availA, a):
                trainsA += 1
            if len(fromA[a]) == 1:
                departA.pop(0)
            else:
                fromA[a].pop(0)
            availB.append(add_T(fromA[a][0], T))
        elif a > b:
            if len(availB) == 0 or isNotAvail(availB, b):
                trainsB += 1
            if len(fromB[b]) == 1:
                departB.pop(0)
            else:
                fromB[b].pop(0)
            availA.append(add_T(fromB[b][0], T))
        else:
            if len(availA) == 0 or isNotAvail(availA, a):
                trainsA += 1
            if len(availB) == 0 or isNotAvail(availB, b):
                trainsB += 1
            if len(fromA[a]) == 1:
                departA.pop(0)
            else:
                fromA[a].pop(0)
            availB.append(add_T(fromA[a][0], T))
            if len(fromB[b]) == 1:
                departB.pop(0)
            else:
                fromB[b].pop(0)
            availA.append(add_T(fromB[b][0], T))
    if len(departA) > 0:
        for a in departA:
            if isNotAvail(availA, a):
                trainsA += 1
    elif len(departB) > 0:
        for b in departB:
            if isNotAvail(availB, b):
                trainsB += 1
    output.write('%u %u\n' % (trainsA, trainsB))
