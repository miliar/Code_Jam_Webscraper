#! /usr/bin/env python

import sys, math

def binary_rep(Clicks):
    if Clicks > 0 :
        exp_max = int(math.log(Clicks)/math.log(2))+1
    else :
        exp_max = 1
        #print('Warning Clicks < 1, clicks %i' % Clicks)
    rep = []
    j = Clicks
    for i in reversed(range(exp_max)):
        base = 2**i
        if base <= j :
            rep.insert(0,True)
            j = j - base
        else :
            rep.insert(0,False)
        #print(base,j)
    return rep

def slow_method(snappers, clicks):
    s = [False for i in range(snappers)]
    for j in range(clicks):
        snappers_powered = 1
        while s[snappers_powered-1] and snappers_powered < snappers :
            snappers_powered = snappers_powered + 1
        for j in range(snappers_powered):
            s[j] = not s[j]
        #print(s)
    return all(s)


#main code    
f = file(sys.argv[1])
lines = f.readlines()
f.close()

T = int(lines[0].strip())
results = []

for i in range(T):
    N,K = [ int(j) for j in lines[i+1].split(' ')]
    bin_rep = binary_rep(K)
    if len(bin_rep) >= N:
        if all(bin_rep[0:N]):
            results.append('ON')
        else :
            results.append('OFF')
    else :
        results.append('OFF')
    print('case (%i of %i) : N %i, K %i, light state %s' % (i+1, T, N, K, results[-1]))
    #checking
    on_state = results[-1] == 'ON'
    if not on_state == slow_method(N, K):
        raise ValueError,'slow method does not correspond to quick method: bin_rep %s' % str(bin_rep)


#writing output file
f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(['Case #%i: %s' % (i+1,s) for i,s in enumerate(results) ]))
f.close()
