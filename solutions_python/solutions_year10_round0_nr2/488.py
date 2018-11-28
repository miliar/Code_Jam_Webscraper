import sys

from gmpy import gcd, mpz  # http://code.google.com/p/gmpy/


sys.stdin = open("fair-large.in")

n_cases = input()

for case in xrange(1, n_cases + 1):
    events = [mpz(int(x)) for x in raw_input().split()[1:]]

    diffs = (a - b for a in events for b in events)

    common = gcd(diffs.next(), diffs.next())

    for diff in diffs:
        common = gcd(common, diff)    

    doomtime = events[0] % common

    if doomtime:
        doomtime = common - doomtime

    assert(len(set(event % common for event in events)) == 1)

    print "Case #%d:" % case, doomtime
