


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    R, C = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    
    A = []
    good=False
    firstgood=0
    
    for j in xrange(R):
        #A.append([s for s in raw_input().split(" ")])
        A.append(list(raw_input()))
        #print A[-1]
        if not all([s=='?' for s in A[-1]]):
            #print 'here'
            if not good:
                good=True
                firstgood=j
                
            last = None
            for k in xrange(len(A[-1])):
                if A[-1][k]!='?':
                    last = A[-1][k]
                else:
                    if last!=None:
                        A[-1][k]=last
                    else:
                        kk=k
                        while A[-1][kk]=='?':
                            kk+=1
                        last=A[-1][kk]
                        A[-1][k]=last
            #print A[-1]
    #now do first lines
    for j in xrange(firstgood):
        A[j] = [a for a in A[firstgood]]
    #now do middleones
    lastgood = firstgood
    for j in xrange(firstgood+1, R):
        if A[j][0]!='?':
            lastgood=j
        else:
            A[j] = [a for a in A[lastgood]]
    
    #print "Case #{}: {} {}".format(i, n + m, n * m)
    print "Case #{}:".format(i)
    for j in xrange(R):
        print ''.join(A[j])
