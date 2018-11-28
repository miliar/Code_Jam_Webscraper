from sys import stdin as fp

N = int(fp.readline())
for i in xrange(N):
    C, F, X = map(float, fp.readline().split())
    tc = 0
    farms = 0
    factor = 1.0/2
    t_cur = X * factor
    while True:
        # print factor
        farms += 1
        factor_new = 1.0/(F*farms + 2)
        with_farm = tc + C * factor + X * factor_new
        # print "with farm " , with_farm , " without " , t_cur
        # print "tc ", tc, " factor ", factor, " factor_new " , factor_new 
        if with_farm < t_cur:
            t_cur = with_farm
            tc = tc + C * factor            
            factor = factor_new 
        else:
            break
    print "Case #%s: %0.7f" % (i+1, t_cur)
