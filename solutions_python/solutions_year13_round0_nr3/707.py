#!/usr/bin/env python
import fileinput
import bisect

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

found = [
    1,
    4,
    9,
    121,
    484,
    10201,
    12321,
    14641,
    40804,
    44944,
    1002001,
    1234321,
    4008004,
    100020001,
    102030201,
    104060401,
    121242121,
    123454321,
    125686521,
    400080004,
    404090404,
    10000200001,
    10221412201,
    12102420121,
    12345654321,
    40000800004,
    1000002000001,
    1002003002001,
    1004006004001,
    1020304030201,
    1022325232201,
    1024348434201,
    1210024200121,
    1212225222121,
    1214428244121,
    1232346432321,
    1234567654321,
    4000008000004,
    4004009004004
]

# Built the above list with
#for root in xrange(1, 31):
#    square = root**2
#    if is_palindrome(root) and is_palindrome(square):
#        found.append(square)

incoming = fileinput.input()
num_cases = int(incoming.next())
for case in xrange(1, num_cases+1):
    (low, high) = [ int(s) for s in incoming.next().split() ]
    low_at = bisect.bisect_left(found, low)
    high_at = bisect.bisect_right(found, high)
    print "Case #%d: %d" % (case, high_at - low_at)

