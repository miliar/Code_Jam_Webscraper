# WAR:
# loop through blocks
# Play lowest highest block if available else lowest block
# DECEITFUL WAR:
# Lie about all of our higher blocks then him so he'll play lower 
from math import floor
with open('D-large.in', 'r') as f:
    with open('a.out', 'w') as o:
        t = int(f.readline())
        for i in xrange(t):
            N = int(f.readline())
            n = sorted([float(x) for x in f.readline().strip().split()])
            k = sorted([float(x) for x in f.readline().strip().split()])
            # Decieptful WAR
            tN, tK = list(n), list(k)
            w = 0 # Deceitful War win
            for y in tN:
                a = [ x for x in tK if x > y]
                if len(a) > 0:
                    tK.remove(a[0])
                else:
                    w += 1
                    tK.remove(tK[0])
            tN, tK = list(n), list(k)
            d = 0
            for y in tK:
                a = [ x for x in tN if x > y]
                if len(a) > 0:
                    d += 1
                    tN.remove(a[0])
                else:
                    break
                    # tN.remove(tN[0])
            o.write("Case #%i: %i %i\n" % (i+1, d, w))
