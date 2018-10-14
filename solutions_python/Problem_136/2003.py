import sys
lines = open(sys.argv[1]).read().strip().split("\n")
numInput = int(lines[0])
for i in range(1,numInput+1):
    cps = 2.0
    c,f,x = [float(j) for j in lines[i].split()]

    bestT = x/cps
    currT = 0
    while True:
        currT += c/cps
        cps += f
        t = currT + x/cps
        if bestT == None or t < bestT:
            bestT = t
        else:
            break;
    print "Case #{0}: {1}".format(i,bestT)
