from codejam import *

def nextone(RP, i, col):
    for j in xrange(i+1, len(RP)):
        if RP[j][0] == col: return RP[j][1]
    return None

#print '###', nextone([('O', 5), ('O', 8), ('B', 100)], 0, 'B')

@main
def BotTrust():
    T = read_int()
    #print T
    for case in xrange(T):
        tmp = read_strs()
        N = int(tmp[0])
        RP = [(tmp[i], int(tmp[i+1])) for i in xrange(1, 2*N, 2)]
        debug(RP)
        posO, posB = 1, 1
        i = 0
        nextc = RP[i][0]
        if RP[i][0] == 'O':
            nextO = RP[i][1]
            nextB = nextone(RP, 0, 'B')
        else:
            nextB = RP[i][1]
            nextO = nextone(RP, 0, 'O')
        num = 0
        incr = False
        while True:
            debug((nextc, i, posO, nextO, posB, nextB))
            if nextc == 'O' and posO == nextO:
                nextO = nextone(RP, i, 'O')
                incr = True
            else:
                if posO < nextO:
                    posO += 1
                elif posO > nextO:
                    posO -= 1
            if nextc == 'B' and posB == nextB:
                nextB = nextone(RP, i, 'B')
                incr = True
            else:
                if posB < nextB:
                    posB += 1
                elif posB > nextB:
                    posB -= 1
            num += 1
            if incr:
                incr = False
                i += 1
                if i == len(RP): break
                nextc = RP[i][0]
        printcase(case, num)
