lines = open("B-large.in").read().split("\n")
outp = open("output2.txt", "w")
caseCount = int(lines[0])
for k in range(caseCount):
    spl = lines[k + 1].split()
    C = float(spl[0])
    F = float(spl[1])
    X = float(spl[2])
    #print "C: %f, F: %f, X: %f" % (C, F, X)
    prevTotal = None
    prod = 2
    accumulatedTime = 0
    while 1:
        nextFarm = C / prod
        timeReq = X / prod
        if not prevTotal:
            accumulatedTime = nextFarm
            total = timeReq
        else:
            total = timeReq + accumulatedTime
            accumulatedTime += nextFarm
        #print "Next farm: %s, Cum secs: %s, Time required: %s, Total time: %s" % (nextFarm, accumulatedTime, timeReq, total)
        if prevTotal and prevTotal < total:
            break
        else:
            prod += F
            prevTotal = total
    out = "Case #%d: %.7f" % (k + 1, prevTotal)
    print out
    outp.write(out + "\n")
    k += 1
outp.flush()