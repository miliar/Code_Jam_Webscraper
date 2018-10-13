#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    return
    print >> sys.stderr, '..',
    for str in strs:
        print >> sys.stderr, str,
    print >> sys.stderr

def memoize(f):
    memos = {}
    def memoized_f( *args ):
        try:
            result = memos[args]
            trace(args, ": got result from memo")
        except KeyError:
            result = f(*args)
            trace(args, ": got result by calling")
            memos[args] = result
        return result
    return memoized_f

if 0:

    max_n = 100

    Factorial = {}
    Factorial[0] = 1
    for n in range(1, max_n+1):
        Factorial[n] = n * Factorial[n-1]
        trace( 'Factorial(%s) = %s' % (n, Factorial[n]) )

    Choose = {}
    for n in range(max_n+1):
        for k in range(n+2):
            if k == 0:
                Choose[(n,k)] = 1
            elif k == n+1:
                Choose[(n,k)] = 0
            else:
                Choose[(n,k)] = Choose[(n-1,k-1)] + Choose[(n-1,k)]
            trace( 'Choose(%s, %s) = %s' % (n, k, Choose[(n,k)]) )
        assert sum( Choose[(n,k)] for k in range(n+1) ) == pow(2,n)


    D = {}
    D[(0,0)] = 1
    D[(1,0)] = 0
    D[(1,1)] = 1
    for n in range(2, max_n+1):
        for k in range(n+1):
            if k == 0:
                D[(n,k)] = (n-1) * (D[(n-1,0)] + D[(n-2,0)])
            else:
                D[(n,k)] = Choose[(n,k)] * D[(n-k,0)]
            trace( 'D(%s,%s) = %s' % (n,k,D[(n,k)]) )
        assert sum( D[(n,k)] for k in range(n+1) ) == Factorial[n]

    E = {}
    E[0] = 0
    E[1] = 0

    for n in range(2, max_n+1):
        # E[n] is the expected number of hits to achieve sortedness
        #      when exactly n elements are out of their correct place.
        # When n > 1,
        # Goro holds down all the correct elements,
        # hits the table,
        # resulting in one of n! possible permutations.
        # Each permutation has a certain number of those n elements
        # in their correct place.
        # D(n,k) of the permutations have exactly k of those n elements
        # in the right place (and n-k in the wrong place). 0<=k<=n
        # (i.e., when k=0, you're no better off than before)
        #
        # E[n] = 1 + 1/n! * Sum(0<=k<=n, D(n,k) * E[n-k])
        #  mult both sides by n! and pull out the k=0 case
        # n! * E[n] = n! + Sum( 0<k<=n ) + D(n,0) * E[n]
        #
        # (n! - D(n,0)) * E[n] = n! + Sum(...)
        #
        #         n! + Sum( 0<k<=n, D(n,k) * E[n-k] )
        # E[n] =  -------------------------------------
        #         n! - D(n,0)
        
        numerator = Factorial[n] + sum( D[(n,k)] * E[n-k] for k in range(1,n+1) )
        denominator = Factorial[n] - D[(n,0)]
        E[n] = float(numerator) / denominator
        trace( 'E[%s] = %s / %s = %s' % (n, numerator, denominator, E[n]) )

    sys.exit()
    

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    N = int(getline())
    elements = map(int, getline().split())
    assert len(elements)== N
    n_out_of_place = 0
    for i in range(N):
        if elements[i] != i+1:
            n_out_of_place += 1

    print 'Case #%d: %s' % (case_num, n_out_of_place)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
