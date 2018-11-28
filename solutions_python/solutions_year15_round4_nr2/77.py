from __future__ import division
from pprint import pprint
from decimal import Decimal
import time
inputfile = file("in", "rb")
outputfile = file("out", "wb")
out_s = "Case #%d: %s"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
rl = lambda: inputfile.readline().replace("\n","")
d = Decimal
def do_case(ncase):
    parts = rl().split()
    N = int(parts[0])
    V, X = float(parts[1]), float(parts[2])
    srcs = []
    for i in xrange(N):
        Ri, Ci = [float(x) for x in rl().split()]
        srcs.append((Ri, Ci))

    print 'N',N
    # small case
    if N == 1:
        R, C = srcs[0]
        if C != X:
            print >>outputfile, out_s % (ncase, str('IMPOSSIBLE'))
            return
        else:
            print >>outputfile, out_s % (ncase, str('%.7f' % (d(V)/d(R))))
            return
    elif N == 2:
        R1, C1 = srcs[0]
        R2, C2 = srcs[1]
        if C1 > C2:
            R1, C1, R2, C2 = R2, C2, R1, C1
        if not (C1 <= X <= C2):
            print >>outputfile, out_s % (ncase, str('IMPOSSIBLE'))
            return
        if C1 == C2 and C1 != X:
            print >>outputfile, out_s % (ncase, str('IMPOSSIBLE'))
            return
        if C1 == C2 and C1 == X:
            R = R1 + R2
            print >>outputfile, out_s % (ncase, str('%.7f' % (d(V)/d(R))))
            return
        t1 = (d(X)*d(V) - d(C2)*d(V))/((d(C1)-d(C2)) * d(R1))
        t2 = (d(X)*d(V) - d(C1)*d(V))/((d(C2)-d(C1)) * d(R2))
        print >>outputfile, out_s % (ncase, str('%.7f' % max(t1, t2)))
        return



    raise Exception("Only small!!!!")

start_time = time.time()
T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    print "Doing case", ncase
    do_case(ncase)
    print "Done, time", time.time()-start_time
    