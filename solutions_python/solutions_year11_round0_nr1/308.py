import sys
NAME = None
#NAME = "-small-attempt"
#NAME = "-large"

def getMagicWord():
    cnt = nextToken(int)
    commands = []
    for i in range(cnt):
        r, b = nextToken(), nextToken(int)
        commands.append( (r, b) )
    res = 0
    extra = { 'O' : 0, 'B' : 0 }
    d = { 'O' : 1, 'B' : 1 }
    cur = commands[0][0]
    prev = 'B' if cur == 'O' else 'O'
    for cmd in commands:
        r, num = cmd
        delta = abs(d[r] - num)
        if cur != r:
            cur, prev = prev, cur
            t = min(delta, extra[cur])
            extra[prev] = 0
            delta -= t
        extra[prev] += delta + 1
        d[r] = num
        res += delta + 1
    return str(res)

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
