import sys

f = open(sys.argv[1])
n = int(f.readline())

for i in xrange(0,n):
    C,F,X = f.readline().strip("\n").split(" ")
    C = float(C)
    F = float(F)
    X = float(X)

    pr = 2.0
    tt = 0.0
    while True:
        if X < C + X*(pr / (pr+ F)):
            tt += X / pr
            break

        tt += C / pr
        pr += F

    print "Case #%d: %.7f" % (i+1, tt)


