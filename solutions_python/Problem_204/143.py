


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    
    N, P = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    R = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    
    A = []
    for j in xrange(N):
        A.append(sorted([int(s) for s in raw_input().split(" ")]))
    
    ind = [0]*N
    
    pckgs = 0
    K = 1
    #print R
    #print A
    while all([a<P for a in ind]):

        mx = [A[j][ind[j]]*1./(K*R[j]) for j in xrange(N)]

        #print mx
        
        if any([a>1.1 for a in mx]):
            #print 'too many'
            K+=1
            continue
        elif any([a<0.9 for a in mx]):
            #print 'too little'
            for j in xrange(N):
                if mx[j]<0.9:
                    ind[j]+=1
            continue
        pckgs+=1
        ind = [a+1 for a in ind]
    
    print "Case #{}: {}".format(i, pckgs)
    #print "Case #{}:".format(i)
    #print N, P, R
    #print A
    
