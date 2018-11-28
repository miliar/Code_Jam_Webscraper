t = int(raw_input())  # read a line with a single integer
for tt in xrange(1, t + 1):
    
    D, N = [int(s) for s in raw_input().split(" ")]
    
    ks = []
    for i in xrange(N):
        ks.append([int(s) for s in raw_input().split(" ")])
    
    ks = sorted(ks)[::-1]
    
    time = (D - ks[0][0])*1./ks[0][1]
    for a in ks:
        time = max(time, (D - a[0])*1./a[1])
    
    #print D, N
    #print ks
    if time>0:
        print "Case #{}: ".format(tt), "{0:.6f}".format(D*1.0/time)
    else:
        print "Case #{}: ".format(tt), "{0:.6f}".format(0)
