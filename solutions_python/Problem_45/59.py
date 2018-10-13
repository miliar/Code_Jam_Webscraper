#!/usr/bin/env python

"""Google Code Jam 2009, Qualification round."""

import sys

def gen_perms(L):
    if len(L) <= 1:
        yield L
    else:
        for p in gen_perms(L[1:]):
            for i in range(len(p)+1):
                yield p[:i] + L[0:1] + p[i:]

def bribe_count(ls, i):
    count = 0
    l = i - 1
    #left tally
    while l >= 0 and ls[l] == 1:
        count += 1
        l -= 1
    r = i + 1
    #right tally
    while r < len(ls) and ls[r] == 1:
        count += 1
        r += 1
    return count
    
def calc_total(P, order):
    total = 0
    ls = [1] * P
    for i in order:
        ls[i-1] = 0
        total += bribe_count(ls, i-1)
    return total

def calc_res(P, Q, cells):
    #just do a simple brute force of all possible orderings.  Not possible
    #for large dataset, but might be ok for small?  I'm tired and I'd like to
    #sleep, but prob. don't have enough points otherwise.
    min_total = 1e8  #FUGLY!
    for perm in gen_perms(cells):
        min_total = min(min_total, calc_total(P, perm))
    return min_total

def main(args):
    if len(args) < 2:
        return 1
    try:
        f = open(args[1])
        #READ appropriate args from initial lines
        num_cases = int(f.readline())
        for case in xrange(num_cases):
            #READ appropriate args for this case
            P, Q = [int(x) for x in f.readline().split()]
            cells = [int(x) for x in f.readline().split()]
            #CALCULATE answer for this case
            print "Case #" + str(case+1) + ": " + str(calc_res(P, Q, cells))
    except IOError:
        print "Invalid file input"
        return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
    #print str(calc_total(8, [3]))
    #print str(calc_total(20, [14, 6, 3]))
    #print str(calc_total(20, [6, 14, 3]))
