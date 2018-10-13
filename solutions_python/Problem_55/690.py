import sys

f = open(sys.argv[1])
ls = [l for l in f]

tc = int(ls[0])

for ca in xrange(tc):
    R,k,n = [int(v) for v in ls[ca * 2 + 1].split()]
    pssg = [int(v) for v in ls[ca * 2 + 2].split()]
    ear = 0
    for i in xrange(R):
        peo = []
        while len(pssg) > 0 and sum(peo) + pssg[0] <= k:
            peo += [pssg[0]]
            pssg = pssg[1:]
        ear += sum(peo)
        pssg = pssg + peo
        peo = []
    print "Case #%d: %d" % (ca+1, ear)

