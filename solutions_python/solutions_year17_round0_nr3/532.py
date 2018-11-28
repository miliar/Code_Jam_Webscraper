#!/usr/bin/env python2
# -*- coding: utf-8 -*-

t = int(raw_input())

for test_case in range(1,t+1):
    #read test case
    N, K = [int(s) for s in raw_input().split(" ")]
    
    #Solve the problem
    minlsrs, maxlsrs = 0, 0
    
    l = 1
    two_l = 1
    k = K
    n = N
    ns, nl = 0,1
#    print n, k, two_l, ns, nl
    
    while k > two_l:
        if n%2 == 0:
            ns = 2*ns + nl
        else:
            nl = 2*nl + ns
        
        n = n/2
        k = k - two_l
        two_l = 2 * two_l
        l += 1
#        print n, k, two_l, ns, nl
    
    # there are nl sequances of n empty stalls and ns sequances of n-1 empty stalls
    # if k is greater than nl, then the last one goes to a sequence of n-1 empty stalls
    n_final = n if k <= nl else n-1
    minlsrs = (n_final - 1)/2
    maxlsrs = n_final/2
    

    print "Case #{}: {} {}".format(test_case, maxlsrs, minlsrs)