import sys
NAME = None
#NAME = "B-small-attempt0"
#NAME = "-large"

def getMagicWord():
    trans = {}
    oppos = {}
    for i in range(nextToken(int)):
        s = nextToken()
        a, b, c = s
        trans[ (a, b) ] = trans[ (b, a) ] = c
    for i in range(nextToken(int)):
        s = nextToken()
        a, b = s
        oppos[ (a, b) ] = oppos[ (b, a) ] = True
    
    res = []
    n = nextToken(int)
    src = nextToken()
    for c in src:
        res.append(c)
        while len(res) > 1:
            a, b = res[-1], res[-2]
            if (a, b) not in trans:
                break
            res = res[:-2]
            res.append(trans[ (a, b) ])
        for i in range(len(res) - 1):
            if (res[i], res[-1]) in oppos:
                res = []
                break

    ans = "["
    for i in res:
        if len(ans) > 1:
            ans += ", "
        ans += i
    ans += "]"

    return ans

################################################
################################################
def nextToken(func = None):
    res = ""
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
