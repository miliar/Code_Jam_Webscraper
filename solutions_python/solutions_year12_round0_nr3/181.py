#!/usr/bin/env python

import fileinput, collections, sys, operator, itertools

def autodict():
    return collections.defaultdict(autodict)

def input():
    it = iter(itertools.imap(str.rstrip, fileinput.input()))
    it.next()
    while True:
        yield map(int, it.next().rstrip().split())

def main():
    for casenum, (a, b) in enumerate(input()):

        res = countRecycled(a, b)



        print "Case #%d: %d" % (casenum+1, res)

def genCyclesImpl(n):
    digits = str(n)
    for i in range(len(digits)):
        newnum = int(digits[i:] + digits[:i])
        if newnum > n:
            yield newnum

memo = {}
def genCycles(n):
    if n not in memo:
        memo[n] = set(genCyclesImpl(n))
    return memo[n]

def countRecycled(a, b):
    res = 0
    for n in xrange(a, b):
        for m in genCycles(n):
            if m <= b:
                res += 1
    return res


main()


