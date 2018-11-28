def my_avg(row):
    items = filter(lambda c: c is not None, row)
    return (sum(items), len(items))
def sum_avg(x):
    S, I = 0, 0
    for s, i in x:
        S += s
        I += i
    return (S, I)

def sum_avg2(x):
    S = 0
    for s, i in x:
        S += s/float(i)
    return (S, len(x))

def a(avg):
    s, i = avg
    if i == 0:
        return 0
    return s/float(i)

def solve(T):
    WP = [my_avg(row) for row in T]
    OWP = []
    for opp in xrange(len(T)):
        wp = []
        for i in range(len(WP)):
            if T[i][opp] is not None:
                wp.append( (WP[i][0] - T[i][opp], WP[i][1]-1) )
        #print 'owp for %i %r %f' %(opp, wp, a(sum_avg2(wp)))
        OWP.append( sum_avg2(wp) )

    OOWP = []
    for opp in xrange(len(T)):
        oowp = []
        for i in range(len(WP)):
            if T[i][opp] is not None:
                oowp.append( OWP[i] )
        OOWP.append( sum_avg2(oowp) )
    RPI = []
    for opp in xrange(len(T)):
        RPI.append( 0.25 * a(WP[opp]) + 0.5 * a(OWP[opp]) + 0.25*a(OOWP[opp]) )
    return RPI

MAP={'0':0, '1':1, '.':None}
for case in xrange(input()):
    n = input()
    T = []
    for i in xrange(n):
        T.append( [MAP[c] for c in raw_input()] )

    RPI = solve(T)

    print "Case #%i:" % (case+1, )
    for rpi in RPI:
        print "%.12f" % (rpi,)
