import sys

sys.stdin.readline() #skip number of tests
for d,line in enumerate(sys.stdin.readlines()):
    parts = line.strip().split()
    C = int(parts[0])
    nonbase = parts[1:C+1]
    del parts[:C+1]
    D = int(parts[0]); opposed = parts[1:D+1]
    base = parts[-1]

    NB = dict((tuple(sorted(n[:2])),n[2]) for n in nonbase)
    #print >>sys.stderr, base, nonbase, opposed, NB
    res = []
    for B in base:
        res.append(B)
        if len(res) == 0:
            continue

        # nonbase
        while True:
            if len(res) < 2: break
            X = tuple(sorted(res[-2:]))
            if X in NB:
                #print >>sys.stderr, "nonbase:", X, NB[X], res
                del res[-2:]
                res.append( NB[X] )
            else:
                break

        # opposing
        for i in opposed:
            if i[0] in res and i[1] in res:
                #print >>sys.stderr, "opposed:", i, res
                res = []
                break

    print "Case #%d: [%s]" % (d+1, ', '.join(res))
