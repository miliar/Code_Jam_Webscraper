import math

def solve(fstr):
    outStr = ""
    ipt = fstr.strip().split('\n')
    ipt = ipt[1:]
    iptInd = 0
    tcs = []
    while (iptInd < len(ipt)):
        turnT = int(ipt[iptInd])
        iptInd += 1
        nTrs = ipt[iptInd].strip().split()
        nTrsInA = int(nTrs[0])
        nTrsInB = int(nTrs[1])
        iptInd += 1
        trsFrL = []
        trsFrL.append(ipt[iptInd:iptInd + nTrsInA])
        trsFrL.append(ipt[iptInd + nTrsInA:iptInd + nTrsInA + nTrsInB])
        for trsFr in trsFrL:
            for trInd in range(len(trsFr)):
                tr = trsFr[trInd]
                tr = tr.split()
                tr[0] = tr[0].split(':')
                tr[1] = tr[1].split(':')
                tr[0] = int(tr[0][0])*60 + int(tr[0][1])
                tr[1] = int(tr[1][0])*60 + int(tr[1][1])
                trsFr[trInd] = tr

        tcs.append((turnT,trsFrL))
        iptInd = iptInd + nTrsInA + nTrsInB
    
    print str(tcs)

    for tcInd in range(len(tcs)):
        tc = tcs[tcInd]
        lA = []
        for tr in tc[1][0]:
            lA.append((tr[0],1))

        for tr in tc[1][1]:
            lA.append((tr[1]+tc[0],-1))

        lA.sort()
        
        nA = 0
        sum = 0
        for it in lA:
            sum -= it[1]
            if (sum < 0):
                nA += 1
                sum = 0

        lB = []
        for tr in tc[1][1]:
            lB.append((tr[0],1))

        for tr in tc[1][0]:
            lB.append((tr[1]+tc[0],-1))

        lB.sort()
        
        nB = 0
        sum = 0
        for it in lB:
            sum -= it[1]
            if (sum < 0):
                nB += 1
                sum = 0

        outStr += "Case #" + str(tcInd+1) +": " + str(nA) + " " + str(nB) + "\n"

    return outStr
    

ipt = None
opt = None
try:
    prog = "B"
    fName = "B-large.in"
    iptF = file("e:\GCJ\\" + prog + "\\" + fName)
    outStr = solve(iptF.read())
    print outStr
    optF = file("e:\GCJ\\" + prog + "\output.txt",'w+')
    optF.write(outStr)
    optF.close()
    if (fName == "input.txt"):    
        otstF = file("e:\GCJ\\" + prog + "\outtest.txt")
        otst = otstF.read()
        otstF.close()
        if (otst == outStr):
            print "+++++++++++++++ CORRETO +++++++++++++++++"
        else:
            print "______________ INCORRETO ________________"
finally:
    if (iptF != None):
        iptF.close()
