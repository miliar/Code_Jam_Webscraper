import sys
NAME = None
#NAME = "B-small-attempt0"
#NAME = "-large"

def getMagicWord():
    n = nextToken(int)
    seq = []
    x = 0
    for i in range(n):
        seq.append(nextToken(int))
        x ^= seq[-1]

    if x != 0:
        return "NO"
    else:
        return str(sum(seq) - min(seq))

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
