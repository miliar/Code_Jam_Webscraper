#!/usr/bin/env python

import fileinput

def isTidy(n):
    """
    Is n a tidy numbers?  A tidy number is a number that, when
    written in base 10 with no leading zeros, has its digits sorted
    in non-decreasing order.

    I'm going to implement this as, from right-to-left, digits are non-increasing.
    """

    lastDigit = None

#    print "--> %s" % (n, )

    while n >= 10:
        n, digit = divmod(n, 10)

        if lastDigit != None:
#            print "--> %s <= %s" % (digit, lastDigit)
            if digit > lastDigit:
                return False

        lastDigit = digit

    # Should be single digit now
    digit = n

    if lastDigit != None:
        # One more check
#        print "--> %s <= %s" % (digit, lastDigit)
        if digit > lastDigit:
            return False

    # Either it's fine, or it was a single digit which is also fine
    return True

def biggestTidy(n):
    """
        What's the largest tidy number <= n?
    """

    while n > 0:
        if (isTidy(n)):
            return n
        n = n - 1

    return 0

#yesSamps = [8, 123, 555, 224488]
#noSamps = [20, 321, 495, 999990]

#print "yes"
#for n in yesSamps:
#    print "%d: %s" % (n, isTidy(n))

#print "no"
#for n in noSamps:
#    print "%d: %s" % (n, isTidy(n))


inp = fileinput.input()

T = int(inp.readline().strip())
t = 1

for line in inp:
    n = int(line.strip())

    tidy = biggestTidy(n)

    print "Case #%s: %s" % (t, tidy)
    t = t + 1

