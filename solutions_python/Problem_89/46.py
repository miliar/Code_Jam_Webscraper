#!/usr/bin/env python
# encoding: utf-8
"""
Waiters en LCM

"""

import sys, time, copy
from pdb import set_trace as DEBUG

def p(*s):
    print >> sys.stderr, s

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return reduce(lcm, args)

def factors(n):  
    fact={1:1}
    check=2  
    while check<=n:
        if n%check==0:
            n/=check
            t = fact.get(check, 0)
            fact[check] = t+1
        else:
            check+=1  
    return fact  

#problem specific functions

def parseInput(f):
    return int(f.readline())

def main(N):
    if N ==1: return 0
    l = lcmm(*range(1,N+1))
    f = factors(l)
    facts = {1:1}
    maxturns = 0
    for i in range(1,N+1):
        fact = factors(i)
        contribute = 0
        for k,v in fact.items():
            if k not in facts:
                contribute+=1
            if facts.get(k,0)<v:
                facts[k] = v
        maxturns+=contribute
    return sum(f.values()) - maxturns

    #for i in range(N, 0, -1):
        #fact = factors(i)
        #for k,v in fact.items():
            #fk = facts.get(k,0)
            #if fk>v:
                #facts[k]-=v
            #elif fk==v:
                #del(facts[k])
            #else:
                #continue
        
        #pass
    #maxturns = i
    #return maxturns


if __name__ == "__main__":
    if len(sys.argv)==1:
        filename = 'test.in'
    else:
        filename = sys.argv[1]

    f = open('primes.txt')
    primes = f.read().split()
    primes = map(int, primes)
    f.close()
    #print primes
    
    f = open(filename)
    cases = int(f.readline())
    for case in range(cases):
        #p("Case #%i" % (case+1))
        args = parseInput(f)
        print "Case #%i: %s" % (case+1, main(args))
