import sys

def gcd(nums):
    # Euclid's binary gcd, non-recursive
    def bgcd(a, b):
        while b != 0:
            a, b = b, a - b * (a / b)
        return a

    # reduce the numbers pair by pair
    return reduce(bgcd, nums)

def reckon(t):
    # get the time since the earliest Great Event
    tmin = max(t)

    # convert t to represent time since that first event, filtering
    # out the zero
    t = [ tmin - tt for tt in t if tmin != tt ]

    # find the gcd of that
    T = gcd(t)

    # find the time since the last anniversary
    since_last = tmin % T

    # special case: problem specifies y >= 0
    if since_last == 0:
        return 0

    return T - since_last

C = int(sys.stdin.readline())
for case in xrange(1, C+1):
    line = map(int, sys.stdin.readline().strip().split(" "))
    count, line = line[0], line[1:]
    assert count == len(line)
    print "Case #%d: %s" % (case, reckon(line))

# infinite precision ints are *great*
