ifile = file('B-small-attempt1.in')
#ifile = file('B-small.in')
#ifile = file('B-large.in')


primenumber = set()
notprimenumber = set()
def isPrime(x):
    global primenumber, notprimenumber
    if x in primenumber: return True
    if x in notprimenumber: return False
    for i in xrange(2,1+x**.5):
        if x % i == 0:
            notprimenumber.add(x) 
            return False
    
    primenumber.add(x)
    return True

import math
num = int(ifile.readline())

for kk in xrange(num):
    A,B,P = map(int,ifile.readline().strip().split(' '))
#    costresult = strdict()
#    prime = {}
#    for x in xrange(A,B+1):
#        print x
#        for p in xrange(P, x):
##            print p
#            if isPrime(p) and x % p == 0:
#                if p in prime:    prime[p].add(x)
#                else: prime[p] = set([x])
#    print 
#    
    prime = {}
    for x in xrange(A,B+1):
        for p in xrange(P, x+1):
            if isPrime(p) and x % p == 0:
                if p in prime: prime[p].add(x)
                else: prime[p] = set([x])
    
    ct = True
    while(ct):
        ct = False
        for p1 in prime:
            for p2 in prime:
                if p1 >= p2: continue
                if prime[p1] == prime[p2]: continue
                if len(prime[p1].intersection(prime[p2])) > 0:                    
                    prime[p1] = prime[p1].union(prime[p2])
                    prime[p2] = prime[p2].union(prime[p1])
                    ct = True

    total = B - A + 1
    cache = []
    for k in prime:
        if len(prime[k]) > 1:
            if prime[k] in cache: continue
            else:                 
                total -= len(prime[k]) - 1
                cache.append(prime[k])
                
    
#    print total
    print "Case #%s: %s"%(kk+1,total)