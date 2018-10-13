def createReg(string):
    reg = []
    factors = []
    fac = 0
    l = ' '
    for s in string:
        if s != l:
            reg.append(s)
            factors.append(fac)
            fac = 1
            l = s
        else:
            fac += 1
    factors = factors[1:]
    factors.append(fac)
    return reg, factors

def compareRegs(reg0,reg1):
    if len(reg0) != len(reg1):
        return False
    for i in xrange(len(reg0)):
        if reg0[i] != reg1[i]:
            return False
    return True

def findDist(num, i, sf):
    return sum(map(lambda x: abs(x[i] - num), sf))

def findMin(reg, stringFactors):
    maxFacs = []
    for fnum in xrange(len(reg)):
        maxFac = 0
        for sfac in stringFactors:
            maxFac = max(maxFac, sfac[fnum])
        maxFacs.append(maxFac)

    minMoves = 0
    for fnum in xrange(len(reg)):
        maxFac = maxFacs[fnum]
        bestFacD = findDist(maxFac, fnum, stringFactors)
        fac = maxFac - 1

        while(True):
            if fac == 0:
                break
            facD = findDist(fac, fnum, stringFactors)
            bestFacD = min(bestFacD, facD)
            fac -= 1
        minMoves += bestFacD
    return minMoves

def findMin2(stringFactors):
    return sum([abs(stringFactors[0][i] - stringFactors[1][i]) for i in xrange(len(stringFactors[0]))])
    

inp = open("A-large.in", 'r')
outp = open("A-large.out", 'w')

T = int(inp.readline())

for testCase in xrange(T):
    N = int(inp.readline())
    strings = [inp.readline()[0:-1] for i in xrange(N)]
    stringFactors = []
    reg0, fac0 = createReg(strings[0])
    stringFactors.append(fac0)
    felgaWins = False
    for st in strings[1:]:
        reg1, fac1 = createReg(st)
        if (not compareRegs(reg0,reg1)):
            felgaWins = True
            break
        else:
            stringFactors.append(fac1)
    if felgaWins:
        outp.write("Case #{}: Fegla Won\n".format(testCase + 1))
    else:
        outp.write("Case #{}: {}\n".format(testCase + 1, findMin(reg0, stringFactors)))

outp.close()
