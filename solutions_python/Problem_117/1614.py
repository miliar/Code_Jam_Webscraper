import sys

L = ""
T = 1
M = 0
N = 0
C = 1

def getCaseData(fp):
    global L, M, N
    tmp = fp.readline()
    tmp = tmp.replace('\n', "")
    tlist = tmp.split(" ")
    N = int(tlist[0])
    M = int(tlist[1])
    #print N, M
    board = [[0 for x in xrange(M)] for x in xrange(N)]

    for i in range(0,N):
        L = fp.readline()
        L = L.replace('\n', "")
        board[i] = L.split(" ")

    return board


def isPatternPossible(board):
    global N, M, L, T
    i = 0
    line = [0 for x in xrange(N)]
    line2 = [0 for x in xrange(N)]
    line3 = [0 for x in xrange(N)]
    grass = [[100 for x in xrange(M)] for x in xrange(N)]
    excluded = []
    highest = 0
    whereToCut = []
    isPossible = False

    for i in range(0,N):
        line[i] = grass[i][0]
        line2[i] = board[i][0]
    #print board initially
    #for i in range(0, N):
    #    print grass[i]
    #print
    #First line
    lowest = getLowest(board[0], M)
    while(lineHas100(grass[0], M) and highest != lowest and M > 1):
        highest = getHighest(board[0], M, excluded)
        excluded.append(highest)
       # print "Highest: {0}".format(highest)
       # print "Excluded: {0}".format(excluded)
        whereToCut = getLines(board[0], highest,  M)
       # print "WhereToCut: {0}".format(whereToCut)
        for el in whereToCut:
            #Create vertical plan
            for i in range(0,N):
                line3[i] = board[i][el]
            grass, isPossible = cutGrass(grass, line3,getHighest(line3, N, []), el, N, True, True)

            #print board initially
            #for i in range(0, N):
            #    print grass[i]
            #print
            if not isPossible:
                return "NO"

    #Vertical first line
    excluded = []
    whereToCut = []
    highest = 100
    lowest = getLowest(line2, N)
    #print "Lowest: {0}".format(lowest)
    while(highest != lowest and N > 1):
        highest = getHighest(line2,N, excluded)
        excluded.append(highest)
        #print "Highest: {0}".format(highest)
        #print "Excluded: {0}".format(excluded)
        whereToCut = getLines(line2, highest, N)
        #print "WhereToCut: {0}".format(whereToCut)
        for el in whereToCut:
            grass, isPossible = cutGrass(grass, board[int(el)], highest, el, M, False, False)
            #print board initially
            #for i in range(0, N):
            #    print grass[i]

            if not isPossible:
                break
        if not isPossible:
            break

    #print "couldnt decide *************"
    if isPossible:
        return "YES"
    #Start again, this time horizontally
    grass = [[100 for x in xrange(M)] for x in xrange(N)]
    excluded = []
    highest = 0
    whereToCut = []

    lowest = getLowest(line2, N)
    #print "Lowest: {0}".format(lowest)
    while(lineHas100(grass[0], M) and highest != lowest and N > 1):
        highest = getHighest(line2,N, excluded)
        excluded.append(highest)
        #print "Highest: {0}".format(highest)
        #print "Excluded: {0}".format(excluded)
        whereToCut = getLines(line2, highest, N)
        #print "WhereToCut: {0}".format(whereToCut)
        for el in whereToCut:
            grass, isPossible = cutGrass(grass, board[int(el)], getHighest(board[int(el)], M, []), el, M, False, True)
            #print board initially
            #for i in range(0, N):
            #    print grass[i]

            if not isPossible:
                return "NO"

    excluded = []
    whereToCut = []
    highest = 100
    lowest = getLowest(board[0], M)
    #print "Lowest: {0}".format(lowest)
    while(highest != lowest and M > 1):
        highest = getHighest(board[0], M, excluded)
        excluded.append(highest)
        #print "Highest: {0}".format(highest)
        #print "Excluded: {0}".format(excluded)
        whereToCut = getLines(board[0], highest,  M)
        #print "WhereToCut: {0}".format(whereToCut)
        for el in whereToCut:
            #Create vertical plan
            for i in range(0,N):
                line3[i] = board[i][el]
            grass, isPossible = cutGrass(grass, line3,highest, el, N, True, False)

            #print board initially
            #for i in range(0, N):
            #    print grass[i]
            #print
            if not isPossible:
                return "NO"
    return "YES"

def getHighest(line, lim, excluded):
    highest = 0
    for i in range(0,lim):
        if int(line[i]) > highest and int(line[i]) not in excluded:
            highest = int(line[i])

    return highest

def getLowest(line, lim):
    lowest = 100
    for i in range(0,lim):
        if int(line[i]) < lowest:
            lowest = int(line[i])

    return lowest

def getLines(line, highest, lim):
    hlist= []
    for j in range(0, lim):
        if int(line[j]) == highest:
            hlist.append(j)

    return hlist

def cutGrass(board, plan, size, i, lim, vertical, first):
    #print """Entering cutGrass\nArgument stack:\nboard: {0}\nsize: {1}
#lim: {2}\ni: {3}\nvertical: {4}\nplan: {5}\nfirst: {6}""".format(board,size,lim,i,vertical, plan, first)
    alreadyOk = True
    if vertical:
        for j in range(0, lim):
            if board[j][i] != int(plan[j]):
                alreadyOk = False
                break
        #Cut grass in vertical
        if not alreadyOk:
            for j in range(0, lim):
                desiredSize = int(plan[j])
                if int(board[j][i]) > size:
                    board[j][i] = size
                if board[j][i] != desiredSize and not first:
                    return board, False
    else:
        #Check if grass is already at desired size
        for j in range(0, lim):
            if board[i][j] != int(plan[j]):
                alreadyOk = False
                break
        #Cut grass in horizontal
        if not alreadyOk:
            for j in range(0, lim):
                desiredSize = int(plan[j])
                if int(board[i][j]) > size:
                    board[i][j] = size
                if board[i][j] != desiredSize and not first:
                    return board, False
    return board, True

def lineHas100(line, lim):
    for i in range(0,lim):
        if int(line[i]) == 100:
            return True
    return False

def main(argv):
    global N, L,T, C
    infile = argv[0]
    #open file
    fp = open(infile)

    T = fp.readline()

    for i in range(0, int(T)):
        lawn = getCaseData(fp)
        status = isPatternPossible(lawn)
        print "Case #{0}: {1}".format(C, status)
        C += 1

if __name__ == "__main__":
    main(sys.argv[1:])
