def strategy(c,f,x,p=2.0):
    t = 0.0
    while ((c/p + x/(p+f)) < x/p):
        t += c/p
        p += f
    t += x/p
    return t

t = input()
for y in xrange(t):
    c,f,x = map(float,raw_input().split())
    print "Case #%d: %.7f" %(y+1,strategy(c,f,x))
    #print "Case #"+str(y+1)+": "+str(strategy(c,f,x))


