f=open("CCAsmall.in",'r+')
cases = f.readline()
for i in xrange(int(cases)):
    C, F, X = map(float, f.readline().split())
    tmax = 999999.0
    j=0
    while True:
        t=0
        for k in xrange(j):
            t+=C/(2+F*k)
        t+=X/(2+F*j)
        if t<tmax:
            tmax=t
        else:
            print "Case #" + str(i+1) + ": " + str(tmax)
            break
        j+=1
f.close()

