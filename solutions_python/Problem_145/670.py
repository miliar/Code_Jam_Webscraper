#!/usr/bin/python
from sys import argv
power2 = [2**x for x in range(41)]
tuple2 = dict((2**x,x) for x in range(41))
def primes_sieve2(limit):
    a = [True] * limit                   
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

primes=list(primes_sieve2(10**6))
f=open(argv[1],"r")
lines = [line[:-1] for line in f.readlines() if len(line)>1]
n = int(lines[0])
for i,line in enumerate(lines[1:]):
    x,y = map(int, line.split('/'))
    if x>y: 
        print "Case #%d: impossible" %(i+1,)
    else: 
        for p in primes:
            if x%p==0 and y%p==0: 
                while x%p==0:
                    x=x/p 
                while y%p==0:
                    y=y/p 
        if y not in power2:
            print "Case #%d: impossible" %(i+1,)
            continue
        m2=0
        for j in range(41):
            if 2**j<=x:
                m2=2**j
            else:
                break
        y/=m2  
        if y not in tuple2:
            print "Case #%d: impossible" %(i+1,)
            continue
        print "Case #%d: %d" %(i+1,tuple2[y])
