import sys
N = 0
T = 1
time = 0
C = 0
F = 0
X = 0


def getCaseData(fp):
    line = fp.readline()
    global C, F, X
    C, F, X = line.split(" ")
    C = float(C)
    F = float(F)
    X = float(X)


def getItems():
    global N, L, T
    global C, F, X
    global time

    myCookies = 0
    myFarms = 0
    cookieRate = 2
    tempT = 0
    time = 0
    while myCookies < X:
        cookieRate = 2 + F * myFarms
        tempT = C / cookieRate

        # We need to calculate if buying a new farm is a good option or not
        fCookieRate = cookieRate + F
        fTempT = X / fCookieRate

        tempT2 = X / cookieRate
        if fTempT + tempT > tempT2:
            time += tempT2
            myCookies = X
            break
        else:
            time += tempT
            myFarms += 1

    tstr = "%.7f" % time
    print "Case #{0}: {1}".format(int(T), tstr)


def main(argv):
    global N, L, T
    infile = argv[0]
    #open file
    fp = open(infile)

    N = fp.readline()
    for i in range(0, int(N)):
        getCaseData(fp)
        getItems()
        T += 1


if __name__ == "__main__":
    main(sys.argv[1:])
