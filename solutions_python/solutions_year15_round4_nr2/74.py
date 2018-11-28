for t in xrange(input()):
    N,V,X = raw_input().split()
    N = int(N)
    V = float(V)
    X = float(X)
    r,c = zip(*[map(float,raw_input().split()) for _ in xrange(N)])
    if N==1:
        if c[0]!=X: print "Case #%d: IMPOSSIBLE"%(t+1)
        else:
            print "Case #%d: %f"%(t+1, V/r[0])
    elif N==2:
        if not min(c)<=X<=max(c): print "Case #%d: IMPOSSIBLE"%(t+1)
        elif c[0]==c[1]:
            print "Case #%d: %f"%(t+1, V/(r[0]+r[1]))
        else:
            a = (X*V - V*c[0])/(c[1]-c[0])
            retval = max((V-a)/r[0],a/r[1])
            print "Case #%d: %f"%(t+1, retval)
        
