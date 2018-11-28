import sys

dbg = False

f = open(sys.argv[1])
ls = [l for l in f]

tc = int(ls[0])

for ca in xrange(tc):
    a = 0
    N, k = [int(v) for v in ls[1 + ca].split()]
    if dbg: print '**********'
    if dbg: print N, k
    if dbg: print '**********'

    if k < (1 << N) - 1 :
        a = 0
    else:
        if N < 2 :
            a = k % 2
        else:
            if k == 1 << N:
                a = 0
            else:
                a = k % (1 << N)

    if (a & ((1 << N) - 1)) == (1 << N) - 1 :
        fst = 'ON'
    else:
        fst = 'OFF'
    print "Case #%d: %s" % (ca+1, fst)
