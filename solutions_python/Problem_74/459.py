fout = open("out.txt","w")
def go(bm,om,c,mc):
    bi, oi = 0,0
    bp, op = 0,0
    m = 0
    t = 0

    for i in xrange(0,mc):
        dist = 0
        if bi < len(bm) and bm[bi][1] == i:
            dist = abs(bm[bi][0] - bp) + 1
            bp = bm[bi][0]
            if oi < len(om):
                if om[oi][0] > op:
                    op = min(op + dist, om[oi][0])
                else:
                    op = max(op - dist, om[oi][0])
            bi += 1
        elif oi < len(om):
            dist = abs(om[oi][0] - op) + 1
            if bi < len(bm):
                if bm[bi][0] > bp:
                    bp = min(bp + dist, bm[bi][0])
                else:
                    bp = max(bp - dist, bm[bi][0])
            op = om[oi][0]
            oi += 1
        t += dist
    fout.write("Case #{0}: {1}\n".format(c,t))

import sys

fin = open(sys.argv[1])


cases = int(fin.readline())
c = 1

for l in fin:
    t = l.split(" ")
    om = []
    bm = []
    mc = int(t[0])
    x = 0
    for i in xrange(1,len(t),2):
        s = int(t[i+1]) - 1
        v = t[i]
        if v == 'O':
            om.append((s,x))
        else:
            bm.append((s,x))
        x+=1
    go(bm,om,c,mc)
    c+=1


