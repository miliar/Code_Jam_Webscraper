from sys import stdin as st

cases = int(st.readline())

for case in xrange(1, cases + 1):

    r, t = [ float(x) for x in st.readline().split() ]

    rings = 0

    while 1:
        s = 2.0*r + 1
        
        if t - s >= 0:
            t -= s
            rings += 1
            r += 2
        else:
            break

    print "Case #%d: %d" % (case, rings)
