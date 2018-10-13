#!/usr/bin/python

import sys
import math

#f = open('A-small.in')

f = sys.stdin


test_cases = int(f.readline().strip())

case_num = 1


cache = {}


#def center( A,B,C ):
#    return ( ( A[0] + B[0] + C[0] ) / 3., (A[1] +  B[1] + C[1] ) / 3. )


def perms(l):
    perms = []
    for i in xrange(0, len(l)):
        for j in xrange(i + 1, len(l)):
            #for k in xrange(j + 1, len(l)):
            yield (l[i], l[j])
                #perms.append([l[i], l[j], l[k]])
    #return perms

def prime_factors(n):
    """ Return the prime factors of the given number. """
    factors = []
    lastresult = n

    # 1 is a special case
    if n == 1:
        return [1]

    while 1:
        if lastresult == 1:
            break

        c = 2

        while 1:
            if lastresult % c == 0:
                break

            c += 1

        factors.append(c)
        lastresult /= c

    return factors


def find_set(i, set):
    for s in set:
        if i in s:
            return set[set.index(s)]
                

for i in range(test_cases):
    ( A, B, P ) = [ int(x) for x in f.readline().strip().split() ]
    theset = range(A,B + 1)
    count = len(theset)
    sets = []
    for i in theset:
        sets.append([i])
        
    
    for x in perms(theset):
        #print x
        p0 = prime_factors(x[0])
        p1 = prime_factors(x[1])
        for i in p0:
            if i in p1 and i >= P:
                #print x, p0, p1, P, i
                p1_set = find_set(x[1], sets)
                p0_set = find_set(x[0], sets)
                if p1_set != p0_set:
                    find_set(x[0],sets).extend(p1_set)
                    sets.remove(p1_set)
                #print sets
                        
                count -= 1
    print "Case #%d: %d" % (case_num, len(sets))
    case_num += 1
