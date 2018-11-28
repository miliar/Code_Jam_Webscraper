#! /usr/bin/env python

import sys, math, copy

def find_factors(p):
    if p > 1 :
        factors = [1,p]
    else :
        return [1]
    for j in xrange(2,p/2):
        if p % j == 2:
            factors.append(j)
    return factors

def method1(Events):
    E = sorted(Events)
    dE = [ E[i+1]-E[i] for i in range(len(E)-1) if E[i+1]-E[i] > 0]
    min_difference = min(dE)
    #next step find, largest common factor amongst the differences
    den = long(1)
    T = min(dE)
    while den < min_difference and not all([dE_i % T == 0 for dE_i in dE]):
        den = den + 1
        while min_difference % den <> 0 :
            den = den + 1
        T = min_difference / den   
        print('    trying T = %i' % T) 
    if True:
        # find j, such that :
        #     -min(E) + T*j >= 0
        #      j = ceil(min(E)/T)
        if min(E) % T <> 0 :
            j = min(E)/T + 1
            y = j * T - min(E)
        else :
            y = 0
    #print(locals())
    #checking values
    cv = [ (Ev+y) % T == 0 for Ev in E]
    if not all(cv) :
        eF = [(Ev+y) % T for Ev in E]
        print(locals())
        raise ValueError, "Check failed : [ (Ev+y) % T == 0 for Ev in E]"

    return y,T

#main code    
f = file(sys.argv[1])
lines = f.readlines()
f.close()

C = int(lines[0].strip())
results = []
debug = False

for i in range(C):
    t_vals = [long(j) for j in lines[i+1].split(' ')][1:]
    print('case (%i of %i) : t_vals %s , len(t_vals) %s' % (i+1, C, t_vals, len(t_vals)))
    y,T = method1(t_vals)
    print('  y,T : %i,%i' % (y,T))
    results.append(y)

#writing output file
f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(['Case #%i: %i' % (i+1,y) for i,y in enumerate(results) ]))
f.close()
