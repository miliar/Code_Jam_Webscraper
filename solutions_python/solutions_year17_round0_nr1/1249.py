t = int(raw_input())  # read a line with a single integer
for itr in xrange(1, t + 1):
    S,K = [str(ip) for ip in raw_input().split(" ")]  # read a list of integers, 2 in this case
    
    #print "\nNewCase"

    K = int(K)
    s = []

    for i,x in enumerate(S):
        s.append(True if x is "+" else False)
    
    lim = len(S) - K
    imp = False
    flips = 0
    
    #print "Initial", s
    for i,x in enumerate(s):
        if(x==False):
            if(i>lim):
                print "Case #{}: IMPOSSIBLE".format(itr)
                imp = True
                break
            flips = flips + 1
            for j,y in enumerate(s[i:i+K]):
                s[j+i] = not s[j+i]
        #print s
    
    if (imp==False):
        print "Case #{}: {}".format(itr,flips)
    
    
