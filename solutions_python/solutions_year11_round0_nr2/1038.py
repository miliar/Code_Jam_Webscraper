"""B
   Google CodeJam 2011
"""

from datetime import datetime


def routine(C, Cs, Csi, D, Ds, Dsi, N, Ns):
    s = ""
    for c in Ns:
        s += c
        if s[-2:] in Csi:
            s = s[:-2] + Csi[s[-2:]]
        else:
            if c in Dsi:
                if any([d for d in Dsi if Dsi[c] in s]):
                    s = ""
                    continue        
    return s

if __name__ == '__main__':
    filename = "B-small-attempt0"
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        ins = f.readline().split()
        C = int(ins.pop(0))
        Cs = []
        Csi = {}
        for i in xrange(C):
            x = ins.pop(0)
            Cs.append(x)
            Csi[x[:2]] = x[2]
            Csi[x[:2][::-1]] = x[2]
        D = int(ins.pop(0))
        Ds = []
        Dsi = {}
        for i in xrange(D):
            x = ins.pop(0)
            Ds.append(x)
            Dsi[x[0]] = x[1]
            Dsi[x[1]] = x[0]
        N = int(ins.pop(0))
        Ns = ins.pop(0)
        
        #print C, Cs, Csi, D, Ds, Dsi, N, Ns
        print C, D, Ns

        print >>fo, "Case #%d: [%s]" % (case+1, ", ".join([x for x in routine(C, Cs, Csi, D, Ds, Dsi, N, Ns)]))

    fo.close()
    f.close()
    print datetime.now()
