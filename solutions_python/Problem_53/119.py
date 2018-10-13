t = int(raw_input())
for i in xrange(1,t+1):
    n,k = [long(x) for x in raw_input().split()]
    p = 2**n;
    if k%p==p-1:
        print "Case #%d: ON"%i
    else:
        print "Case #%d: OFF"%i
