import logging

logging.basicConfig(format='%(message)s')

# given a number n, we want the largest tidy number less than or equal to n.
# a number is tidy if its digits are non-decreasing when reading the number
# from left to right
def do_case(nstr):
    # set the soln equal to the input
    # examine the digits in order from left to right.
    # if the next number is less than the current one, then decrement
    # the current one (borrow if necessary) and set all the remaining
    # digits to 9's.

    # in case of no work, this is the soln
    soln = nstr

    # handle single digits as a special case
    if len(soln) == 1: return soln

    i = 1
    c_last = int(nstr[i-1])
    c = int(nstr[i])
    while ((c >= c_last) and (i < len(nstr)-1)):
        #print "compared %d >= %d" % (c, c_last)
        i += 1
        c_last = c
        c = int(nstr[i])

    if (c >= c_last) and (i == len(nstr)-1): return soln
    #print "terminated at i=%d" % i

    # otherwise, we need to decrement because c < c_last
    d = int(nstr[:i]) - 1
    #print "d=%d" % d
    if d != 0:
        soln = do_case("%d%s" % (d, "9"*(len(nstr)-i)))
    else:
        soln = do_case("%s" % "9"*(len(nstr)-i))

    return soln

# main starts here

T = int(raw_input())

for i in xrange(T):
    Nstr = raw_input()

    soln = do_case(Nstr)

    print("Case #%d: %s" % (i+1, soln))
    logging.warn("Case #%d: %s" % (i+1, soln))

