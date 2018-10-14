for T in xrange(input()):
    c,f,x = map(float,raw_input().split())
    s = 0
    n = 2
    while x/n>c/n+x/(n+f):s+=c/n;n+=f
    print "Case #%d: %.7f"%(T+1,s+x/n)
    
