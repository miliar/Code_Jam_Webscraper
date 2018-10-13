from math import pi


t = int(raw_input())  # read a line with a single integer
for tt in xrange(1, t + 1):
    
    N, K = [int(s) for s in raw_input().split(" ")]
    
    A = []
    for nn in xrange(N):
        Ri, Hi = [int(s) for s in raw_input().split(" ")]
        A.append([Ri*Ri, 2.*Hi*Ri])
        #H.append([2*Hi*Ri, nn])
    
    maxar = 0
    A = sorted(A)[::-1]
    B = [[a[1],a[0]] for a in A]
    
    #print A, B
    
    for kk in xrange(N-K+1):
        #CC = sorted(B[kk:])[::-1]
        CC = sorted([B[kkk][0] for kkk in xrange(kk+1, N)])[::-1]
        maxar = max(maxar, A[kk][0]+B[kk][0] + sum(CC[0:K-1]))
        #print CC, maxar
        
    print "Case #{}: ".format(tt), "{0:.9f}".format(pi*maxar)
    
    
    
    