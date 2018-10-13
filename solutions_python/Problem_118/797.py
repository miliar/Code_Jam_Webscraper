#!/usr/bin/env python

import sys
import logging
from math import sqrt

def is_palindrome(x):
    if x % 10 == 0:
        return False
    n = x
    r = 0
    while n > 0:
        r = r*10 + (n%10)
        n /= 10
    return r == x


def is_fair_square(x):
    return is_palindrome(x) and is_palindrome(x*x)


fair_numbers = [x for x in xrange(1, 1001) if is_fair_square(x)]


def solve(A, B):
    return len([x for x in fair_numbers if x*x >= A and x*x <= B])
    # count = 0
    # u = int(sqrt(A))
    # if u*u < A:
    #     u += 1
    # v = int(sqrt(B))
    # if v*v == B:
    #     v += 1
        
    # for x in xrange(u, v):
    #     if is_fair_square(x):
    #         logging.info("xx: %d %d", x, x*x)
    #         count += 1
    # return count



def main(lines, output):
    T = int(lines.next())
    for case in xrange(1,T+1):
        inputs = map(int, lines.next().split())
        r = solve(*inputs)
        s = "Case #%d: %s" % (case, r)
        output.write(s + "\n")
        logging.info(s)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "expects filename"
        sys.exit(1)
    logging.basicConfig(level=logging.DEBUG)
    
    outfile = sys.argv[1] + ".out"
    main(open(sys.argv[1]), open(outfile, "w"))

