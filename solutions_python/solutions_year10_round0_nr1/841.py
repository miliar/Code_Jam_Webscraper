t=int(raw_input())
for i in xrange(0,t):
    l=raw_input().split()
    n=int(l[0])
    k=int(l[1])
    if (k+1)%(2**n) ==0:
        print "Case #%d: ON" %(i+1)
    else:
        print "Case #%d: OFF" %(i+1)
