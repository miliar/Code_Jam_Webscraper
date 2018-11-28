import sys
with open(sys.argv[1], 'rt') as f:
    nOfCases = int(f.readline().strip())
    for case in range(nOfCases):
        tmp = f.readline()
        tmp = tmp.split()
        m = int(tmp[0])
        p = [int(x) for x in tmp[1]] 
        n = 0
        cum = 0
        for c in range(0, m + 1 ):
            #print "need standing: {}, have standing {}".format(c, cum+n)
            if cum + n < c:
                n += c - (cum + n)
            cum += p[c]
        print "Case #{}: {}".format( case + 1, n )


