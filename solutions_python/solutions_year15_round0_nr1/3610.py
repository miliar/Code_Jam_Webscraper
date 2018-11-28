

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def foo(arr,N,P,Parr):
    result = P*[0]
    #print result
    #print Parr
    for i in range(P):
        for j in [2*x for x in range(N)]:
            #print arr[j],arr[j+1]
            if Parr[i] >= arr[j] and Parr[i] <= arr[j+1]:
                result[i]+=1
    
    return ' '.join([str(i) for i in result])
            
        



if __name__ == "__main__":
    T = input()
    #print T
     
    for caseNr in xrange(1, T+1):
        arr = [x for x in raw_input().split()]
        #print arr
        Smax = int(arr[0])
        p = [int(i) for i in str(arr[1])]
        #print p
        sigmaP = p[0]
        A = 0
        for shy in range(1,Smax+1):
            if p[shy] != 0:
                #print shy,sigmaP
                if shy > sigmaP:
                    A = A + shy - sigmaP
                    sigmaP = sigmaP + A + p[shy]
                else:
                    sigmaP = sigmaP + p[shy]

        
##        try:
##            space = raw_input()
##        except EOFError:
##            pass
        #print Parr
        print "Case #%i: %s" % (caseNr, A)
        #print sigmaP,A

