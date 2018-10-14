import sys
NAME = None
#NAME = "-small-attempt"
#NAME = "-large"

def getMagicWord():
    X = nextToken(int)
    S = nextToken(int)
    R = nextToken(int)
    t = nextToken(float)
    N = nextToken(int)
    segs = []
    totalSum = 0
    for i in range(N):
        b = nextToken(int)
        e = nextToken(int)
        w = nextToken(int)
        segs.append( (e - b, w))
        totalSum += e - b
    segs.append( (X - totalSum, 0) )
    segs.sort(key = lambda x: x[1])
    res = 0
    for s in segs:
        L, w = s[0], s[1]
        runt = L / (w + R)
        runt = min(t, runt)
        t -= runt
        res += runt
        L -= (w + R) * runt
        res += L / (w + S)

    return "%.6f" % res

################################################
################################################
def nextToken(func = None):
    c = ""
    while fin:
        c = fin.read(1)
        if not c.isspace():
            break
    res = "" + c
    while fin:
        c = fin.read(1)
        if c.isspace():
            break
        res += c
    if func:
        return func(res)
    else:
        return res

def nextLine():
    if fin:
        return fin.readline()
    else:
        return ""

if NAME:
    fin, fout = open(NAME + ".in", "r"), open(NAME + ".out", "w")
else:
    fin, fout = sys.stdin, sys.stdout

#########################
for testNum in range(nextToken(int)):
    print("Case #%d: %s" % (testNum + 1, getMagicWord()))
