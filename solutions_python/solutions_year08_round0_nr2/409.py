def parseTime(timeStr):
    return [int(x) for x in timeStr.split(':')]

def analyzeSheduleString(sheduleStr, shedule, pool, addTime):
    shedule.append([parseTime(x) for x in sheduleStr.split()])
    pool.append([shedule[-1][1][0], shedule[-1][1][1] + addTime])

def calcSheduleTrains(shedule, pool):
    if len(pool) == 0:
        return len(shedule)
    poolPos = 0
    result = 0
    for i in range(len(shedule)):
        if shedule[i][0] >= pool[poolPos]:
            poolPos += 1
            if poolPos == len(pool):
                return result + len(shedule) - i - 1
        else:
            result += 1
    return result

fin = open("input.txt", "r")
fout = open("output.txt", "w")
casesCount = int(fin.readline())
for curCase in range(1, casesCount + 1):
    turnAroundTime = int(fin.readline())
    (aShedCount, bShedCount) = (int(x) for x in fin.readline().split())
    aShed = []
    bShed = []
    aPool = []
    bPool = []
    for i in range(aShedCount):
        analyzeSheduleString(fin.readline(), aShed, bPool, turnAroundTime)
    for i in range(bShedCount):
        analyzeSheduleString(fin.readline(), bShed, aPool, turnAroundTime)
    aShed.sort()
    bShed.sort()
    aPool.sort()
    bPool.sort()
    fout.write("Case #%i: %i %i\n" % (curCase, calcSheduleTrains(aShed, aPool), calcSheduleTrains(bShed, bPool)))
fin.close()
fout.close()