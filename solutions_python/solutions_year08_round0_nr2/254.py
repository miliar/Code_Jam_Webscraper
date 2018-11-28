import sys

def Conv2Mins(time):
    hh, mm = time.split(":")
    return int(hh) * 60 + int(mm)

def GetTrainsRequired(T, scheduleX, scheduleY):
    arrQ = []
    depQ = []

    for s in scheduleX:
        depQ.append(s[0])

    for s in scheduleY:
        arrQ.append(s[1])
        
    arrQ.sort()
    depQ.sort()
    
    trainsReq = 0
    
    for dep in depQ:
        if len(arrQ) == 0:
            trainsReq += 1
        else:
            arr = arrQ[0] + T
            if arr > dep:
                trainsReq += 1
            else:
                arrQ.pop(0)

    return trainsReq

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(-1)

    fin = open(sys.argv[1], "r")
    inCases = int(fin.readline().strip())
    
    for i in range(1, inCases + 1):
        T = fin.readline().strip()
        NA, NB = fin.readline().strip().split()

        scheduleA = []
        for j in range(0, int(NA)):
            dep, arr = fin.readline().strip().split()
            depMins = Conv2Mins(dep)
            arrMins = Conv2Mins(arr)
            scheduleA.append((depMins, arrMins))
            
        scheduleB = []
        for j in range(0, int(NB)):
            dep, arr = fin.readline().strip().split()
            depMins = Conv2Mins(dep)
            arrMins = Conv2Mins(arr)
            scheduleB.append((depMins, arrMins))
            
        trainsA = GetTrainsRequired(int(T), scheduleA, scheduleB)
        trainsB = GetTrainsRequired(int(T), scheduleB, scheduleA)
        
        print "Case #%d: %d %d" % (i, trainsA, trainsB)
    fin.close()
    