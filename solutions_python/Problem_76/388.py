#!/usr/bin/python -u

import sys, re, itertools, operator

#----------------------------------------------------------------------

def solveBruteForce(cvalues):
    # not possible for N = 1000

    # just try out all combinations (all possible subsets
    # of candies for Sean)

    bestSolution = None

    allSum = sum(cvalues)

    allSumPatrick = reduce(operator.xor, cvalues)

    # note that both piles must have at least one element
    for theLen in range(1,len(cvalues)):

        for patricksCandies in itertools.combinations(cvalues, theLen):

            # calculate the true sum (what Sean wants to maximize)
            trueSum = allSum - sum(patricksCandies)

            # calculate Patrick's value (XOR) of patrick's candies
            patricksValue = 0
            for candy in patricksCandies:
                patricksValue ^= candy

            # note that xor is both plus and minus modulo 2
            # (in Patrick's arithmetic)
            seansValue = allSumPatrick ^ patricksValue

            if seansValue == patricksValue:

                bestSolution = max(bestSolution, trueSum)


    if bestSolution == None:
        return "NO"
    else:
        return bestSolution

#----------------------------------------------------------------------

def solveSmart(cvalues):

    # for Patrick, both of the XORs must be the same,
    # i.e. the XOR of the entire set must be zero

    if reduce(operator.xor,cvalues) != 0:
        return "NO"

    # because subtraction and addition is the same modulo 2
    # (i.e. xor), we can partition cvalues in any
    # way and xored the two partitions will always
    # have the same value
    #
    # -> give the candy with the smallest value to Patrick,
    # keep the rest for Sean
    #
    # note that none of the candies has a negative value..

    # sort them (we can afford it here in the contest)

    allSum = sum(cvalues)

    cvalues.sort()

    patricksCandies = [ cvalues.pop(0) ]

    # Seans true sum
    trueSum = allSum - sum(patricksCandies)

    # assert(reduce(operator.xor,patricksCandies) == 
    #        reduce(operator.xor,cvalues))
    return trueSum
    

#----------------------------------------------------------------------
# main
#----------------------------------------------------------------------

T = int(sys.stdin.readline())

for case in range(1,T+1):

    N = int(sys.stdin.readline())

    C = re.split('\s+',sys.stdin.readline().split('\n')[0])
    C = [ int(x) for x in C ]

    if len(C) != N:
        print >> sys.stderr,"unexpected number of elements"

    # sol = solveBruteForce(C)
    sol = solveSmart(C)

    print "Case #%d:" %case,sol
