"""B
   Google CodeJam 2014
"""

from datetime import datetime


def routine(C, F, X):
    comp = 0
    prevmost = X
    tot =  0
    t = 0
    while True:
        s = (2+(F*t))
        tnow = C / s

        most = X / s
        
        if prevmost < comp + most:
            return prevmost

        prevmost = comp + most
        
        comp += tnow
        t += 1
        

if __name__ == '__main__':
    filename = "B-large"  #-small-attempt0 -large
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        ins = f.readline().split()
        C = float(ins.pop(0))
        F = float(ins.pop(0))
        X = float(ins.pop(0))
        
        print C, F, X

        print >>fo, "Case #%d: %s" % (case+1, routine(C, F, X))

    fo.close()
    f.close()
    print datetime.now()
