import sys


fp = open(sys.argv[1])
N = int(fp.readline().strip())

def foo():
    DN = fp.readline().strip().split(" ")
    D = float(DN[0])
    N = int(DN[1])
    maxt = 0.0
    for i in range(N):
        KS = fp.readline().strip().split(" ")
        K = float(KS[0])
        S = float(KS[1])
        t = (D-K)/S
        maxt = max(maxt, t)
    return D/maxt

for case in range(N):
    print "Case #%d: %f" % (case + 1, foo())

fp.close()
