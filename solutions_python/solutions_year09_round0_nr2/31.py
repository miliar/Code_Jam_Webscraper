import sys, re

def lin(): return sys.stdin.readline()

T = int(lin())
m = d = []
H = W = 0
last = 0

def fill(x, y):
    global m, d, last
    if d[x][y]>0: return
    wx = x; wy = y
    for (a,b) in [(x-1, y), (x,y-1), (x,y+1), (x+1,y)]:
        if 0<=a<H and 0<=b<W and m[a][b]<m[wx][wy]:
            (wx,wy) = (a,b)
    if wx==x and wy==y:
        last += 1
        d[x][y] = last
        return
    fill(wx,wy)
    d[x][y] = d[wx][wy]
    return

for casenum in range(T):
    (H, W) = [int(s) for s in lin().split()]
    m = []
    for h in range(H):
        l = [int(s) for s in lin().split()]
        assert(len(l)==W)
        m.append(l)
    d = [ [0 for i in range(W)] for j in range(H) ]
    last = 0
    for i in range(H):
        for j in range(W):
            fill(i, j)

    for h in range(H):
        for w in range(W):
            d[h][w] = chr(d[h][w] + ord('a') - 1)

    print "Case #%d: " % (casenum+1)
    for h in range(H):
        for w in range(W):
            print d[h][w],
        print
