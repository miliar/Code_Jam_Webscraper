from collections import defaultdict
import math
import os
import sys

def get_primes(n):
    numbers = set(xrange(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(xrange(p*2, n+1, p)))
    return primes

limit = 1000

primes = get_primes(limit)

with open("in.txt") as f:
    with open("out.txt", "w") as out:
        for case in range(1, int(f.readline()) + 1):
            out.write("Case #%s: " % case)
            n = int(f.readline())

            if n == 1:
                out.write("0")
            else:
            
                factors = []
        
                for p in primes:
                    q = p
                    while 1:
                        if q <= n:
                            factors.append(p)
                            q *= p
                        else:
                            break
                        
                print n, factors
                print 1 + len(factors) - len(set(factors))
                
                out.write("%d" % (1 + len(factors) - len(set(factors))))
                         
            out.write("\n")