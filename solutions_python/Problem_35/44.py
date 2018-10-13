import sys
sys.setrecursionlimit(20000)
inp = open("d:\\incoming\\b-large.in", "r")
#inp = open("d:\\incoming\\b-small-attempt0.in", "r")
#inp = open(".\\b.in", "r")
outp = open(".\\b.out", "w")

global sink, m, label, dx, dy, h, w

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]


def getSink(y, x):
    if sink[y][x] != (-1, -1):
        return sink[y][x]

    minHeight = m[y][x]
    res = (y, x)
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if ny < 0 or nx < 0 or ny >= h or nx >= w:
            continue
        if m[ny][nx] < minHeight:
            res = getSink(ny, nx)
            minHeight = m[ny][nx]
    sink[y][x] = res
    return res

def flood(y, x, mark):
    label[y][x] = mark
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if ny < 0 or nx < 0 or ny >= h or nx >= w:
            continue
        if label[ny][nx] != " ":
            continue
        if getSink(ny, nx) != getSink(y, x):
            continue
        flood(ny, nx, mark)
    

cases = int(inp.readline())
for cc in xrange(cases):
    h, w = map(int, inp.readline().split())
    m = []
    sink = [ [(-1,-1)] * w for i in xrange(h) ]
    label = [ [" "] * w for i in xrange(h) ]

    for y in xrange(h):
        m.append(map(int, inp.readline().split()))

    regions = 0
    for y in xrange(h):
        for x in xrange(w):
            if label[y][x] == " ":
                flood(y, x, chr(ord('a') + regions))
                regions += 1

    print "Case %d/%d .." % (cc+1, cases)
    outp.write("Case #%d:\n" % (cc+1))
    for y in xrange(h):
        outp.write(" ".join(label[y]) + "\n")
    
    
outp.close()
