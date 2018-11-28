import os

def getTime(C, F, X, numFarms):
    #farm construction time
    time = 0
    for curFarms in range(numFarms):
        time += C/(2+curFarms*F)

    #accumulation
    time += X/(2+numFarms*F)

    return time

def getUpperBound(C, F, X):
    prev = float("inf")
    numFarms = 1
    while True:
        res = getTime(C, F, X, numFarms)
        if res > prev:
            return numFarms + 1
        else:
            prev = res
            numFarms *= 2

def getMinTime(L, U, C, F, X):
    if U - L == 1:
        return getTime(C, F, X, L)
    elif U - L < 1:
        raise Exception("ERROR!!!")
    
    midL = (L+U)/2 - 1
    midR = (L+U)/2

    resultL = getTime(C, F, X, midL)
    resultR = getTime(C, F, X, midR)

    if resultL < resultR:
        return getMinTime(L, midL+1, C, F, X)
    else:
        return getMinTime(midR, U, C, F, X)
    
    

        

infilename = "B-large.in"
in_file = open(infilename)

numcases = int(in_file.readline())
totalout = ""

for casenum in range(numcases):
    C, F, X = [float(w) for w in in_file.readline().split()]
    print C, X

    bound = getUpperBound(C, F, X)
    time = getMinTime(0, bound, C, F, X)

    outstr = "Case #" + str(casenum + 1) + ": " + str(time)
    totalout += outstr + "\n"
    print(outstr)

writetofile = False
if "small" in infilename:
    outprefix = "small"
    writetofile = True
elif "large" in infilename:
    outprefix = "large"
    writetofile = True
#writetofile = False

if writetofile:
    filenum = 0
    while True:
        outfilename = outprefix + str(filenum) + ".out"
        filenum += 1
        if not os.path.isfile(outfilename):
            break
    out_file = open(outfilename, 'w+')
    out_file.write(totalout)
    out_file.close()

in_file.close()
