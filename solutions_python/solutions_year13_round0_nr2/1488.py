#!/usr/bin/python

def readNM(fd):
    N = 0
    M = 0
    a = []
    p = []
    t = fd.readline()

    i_base = 0
    i = 0
    for i in range(0, len(t)):
        if t[i:i+1] == " " or t[i:i+1] == "\n":
            break
    N = int(t[i_base:i])

    i_base = i + 1
    for i in range(i_base, len(t)):
        if t[i:i+1] == " " or t[i:i+1] == "\n":
            break
    M = int(t[i_base:i])

    for n in range(0, N):
        a.append([])
        t = fd.readline()
        j_base = 0
        for j in range(0, len(t)):
            if t[j:j+1] == " " or t[j:j+1] == "\n":
                #print t[j_base:j]
                a[n].append(int(t[j_base:j]))
                j_base = j
            else:
                continue

    return [N, M, a]

def readT(fd):
    T = fd.readline()
    return int(T)

def findMax(N, M, a, curMax):
    newMax = 1
    #print a, curMax
    for i in range(0, N):
        for j in range(0, M):
            if a[i][j] <= curMax and a[i][j] >= newMax:
                newMax = a[i][j]

    return newMax

def findMaxWithMask(N, M, a, mask, curMax, prevIndices):
    newMax = 1
    #print a, mask, curMax, prevIndices
    newI = -1
    newJ = -1
    for i in range(0, N):
        for j in range(0, M):
            if mask[i][j] == 0 and a[i][j] <= curMax and a[i][j] >= newMax and [i, j] not in prevIndices:
                newMax = a[i][j]
                #print newMax, i, j
                newI = i
                newJ = j
    
    if i == N and j == M:
        newI = -1
        newJ = -1

    return newMax, newI, newJ


def fillP(N, M, max):
    p = []
    for i in range(0, N):
        p.append([])
        for j in range(0, M):
            p[i].append(max)

    return p

def getMask(N, M, a, p):
    mask = []
    for i in range(0, N):
        mask.append([])
        for j in range(0, M):
            if a[i][j] == p[i][j]:
                mask[i].append(1)
            else:
                mask[i].append(0)

    return mask

def isMatch(N, M, mask):
    for i in range(0, N):
        for j in range(0, M):
            if mask[i][j] != 1:
                return False
            else:
                continue
    return True


def findcurMaxInA(N, M, a, curMax):
    for i in range(0, N):
        for j in range(0, M):
            if a[i][j] == curMax:
                return (i, j)
            else:
                continue
    return (-1, -1)

def recomputeP(N, M, p, mask, curMax, I, J):
    if p[I][J] > curMax and mask[I][J] == 0:
        # scan row
        okToTrimRow = True
        for k in range(0, M):
            if mask[I][k] != 0:
                if p[I][k] <= curMax:
                    okToTrimRow = True
                else:
                    okToTrimRow = False
                    break
        if okToTrimRow:
            #print 'okToTrimRow'
            for k in range(0, M):
                p[I][k] = curMax
            return p, -1, -1

        #scan column
        okToTrimCol = True
        for k in range(0, N):
            if mask[k][J] != 0:
                if p[k][J] <= curMax:
                    okToTrimCol = True
                else:
                    okToTrimCol = False
                    break
        if okToTrimCol:
            #print 'okToTrimCol'
            for k in range(0, N):
                p[k][J] = curMax
            return p, -1, -1

        #if not okToTrimRow and not okToTrimCol:
            #print '!okToTrimRow and !okToTrimCol'

    return p, I, J

def main(argv):
    argc = len(argv)
    if argc == 1:
        print "No input file!"
        exit(-1)
    if argc > 2:
        exit(-1)
    
    inFilename = argv[1]
    inFd = open(inFilename, "r")

    T = readT(inFd)
    #print 'T='+str(T)


    # for each test case
    for k in range(0, T):
    #for k in range(0, 1):
        [N, M, a] = readNM(inFd)
        #print '(N, M)=('+str(N)+','+str(M)+')'
        #print 'a=',
        #print a

        curMax = 100
        curMax = findMax(N, M, a, curMax)
        #print 'curMax='+str(curMax)

        p = fillP(N, M, curMax)
        #print 'p=',
        #print p

        mask = getMask(N, M, a, p)
        #print 'mask=',
        #print mask

        # do while pattern is not matched
        #print isMatch(N, M, mask)
        I = -1
        J = -1
        prevIndices = []
        while (isMatch(N, M, mask) == False or I == -1 or J == -1):
        #for zzz in range(0, 10):
            prevIndices.append([I, J])
            (curMax, I, J) = findMaxWithMask(N, M, a, mask, curMax, prevIndices)
            #print 'curMax='+str(curMax)
            #(I, J) = findcurMaxInA(N, M, a, curMax)
            #print '(I, J)=('+str(I)+','+str(J)+')'
            #print 'prevIndices=',
            #print prevIndices
            if I == -1 or J == -1:
                break
            if [I, J] in prevIndices:
                break

            (p, I, J) = recomputeP(N, M, p, mask, curMax, I, J)
            #print 'p=',
            #print p
            if I == -1 and J == -1:
                prevIndices = []

            mask = getMask(N, M, a, p)
            #print 'mask=',
            #print mask
            #print

        # check case and declare result
        if isMatch(N, M, mask) == True:
            s = "YES"
        else:
            s = "NO"

        print 'Case #'+str(k+1)+':',
        print s

    inFd.close()
    exit(0)


if __name__ == "__main__":
    import sys
    main(sys.argv)



    

