import sys
sin = sys.stdin
T = int(sin.readline().strip())
for i in xrange(1, T+1):
    D, N = map(long, sin.readline().strip().split())
    if i in [10, 34, 50, 58]:
        print 'D:{0}, N:{1}'.format(D, N)
    tmax = 0
    for j in xrange(N):
        Ki, Si = map(long, sin.readline().strip().split())
        if i in [10, 34, 50, 58]:
            print 'Ki:{0}, Si:{1}'.format(Ki, Si)
        ti = (D-Ki)*1.0/Si
        tmax = max(ti, tmax)
        #print '{0}: ti {1}, tmax {2}'.format(j, ti, tmax)
    t = round(D*1.0*10**6/tmax)/10**6
    print 'Case #{0}: {1:.6f}'.format(i, t)
