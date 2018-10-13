#! /usr/bin/env python

import sys, math

f = file(sys.argv[1])
lines = [ln.strip() for ln in f.readlines()]
T = int(lines[0])
print('%s contains %i (T) test cases' % (sys.argv[1],T))

cases = []
ind = 1
for i in range(T):
    #print(lines[ind], lines[ind].split(' '))
    L,P,C = [int(k) for k in lines[ind].split(' ')]
    cases.append([L,P,C])
    ind = ind + 1
print(cases)

def testProblem(L,P,C):
    '''
    You can run a series of load tests, each of which will determine whether the site can support at least X people for some integer value of X that you choose. If you pick an optimal strategy, choosing what tests to run based on the results of previous tests, how many load tests do you need in the worst case?
    
    The first line of the input gives the number of test cases, T. T lines follow, each of which contains space-separated integers L, P and C in that order.

    For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of load tests you need to run in the worst case before knowing within a factor of C how many people the site can support. 
    '''
    tests = 0
    while 1.0*P/L  > C :
        k = (1.0*P/L)**0.5
        print('L,P,l',L,P,k)
        Ln = int(math.floor(P/k))
        if Ln == L:
            Ln = L+1
        Pn = int(math.ceil(L*k))
        if Pn == P:
            Pn = P -1
        if 1.0*P/Ln > 1.0*Pn/L: #pick worst case
            L = Ln
        else:
            P = Pn
        tests = tests + 1
    return tests

def method2(L,P,C):
    tests = 0
    def split(L,P,count):
        if 1.0*P/L  > C:
            k = (1.0*P/L)**0.5
            #print( P/k , L*k)
            #assert P/k == L*k
            #print('method 2 L,P,l',L,P,k)
            #2 Choices
            X1 = int(math.floor(P/k))
            if X1 == L:
                X1 = L + 1
            X2 = int(math.ceil(P/k))
            if X2 == P:
                X2 = P - 1
            #print(X1,X2)
            #select choice with least test required
            tests1 = max(split(L,X1,count+1),split(X1,P,count+1))
            tests2 = max(split(L,X2,count+1),split(X2,P,count+1))
            return min(tests1,tests2)
        else:
            return count 
    return split(L,P,0)


results = []
for t in range(T):
    print('case %i of %i' % (t+1,T))
    print(cases[t])
    res = testProblem(*cases[t])
    res2 = method2(*cases[t])
    print(res,res2)
    #if res <> res2 :
    #    print(res,res2)
    #    raise ValueError,'res <> res2!!!'
    results.append('Case #%i: %i' % (t+1,res2))
    print(results[-1])

f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(results))
f.close()
