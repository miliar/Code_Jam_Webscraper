import sys

T = int(sys.stdin.readline())

for i in xrange(T):
    line = sys.stdin.readline().split()
    N, S, p, scores = int(line[0]), int(line[1]), int(line[2]), line[3:]

    res = 0

    #print "Case: %d dancers, %d surprising, %d target score" % (N, S, p)

    for score in scores:
        s = int(score)
        #print "* Checking score %d" % s

        if s-p < 0:
            continue

        if (s - p) >= (p-1)*2:
            #print "*** natural %d >= %d" % (s-p, (p-1)*2)
            res = res + 1
        elif S > 0:
            if (s - p) >= (p-2)*2:
                #print "*** surprising %d >= %d" % (s-p, (p-2)*2)
                res = res + 1
                S = S - 1

    print "Case #%d: %d" % (i+1, res)



