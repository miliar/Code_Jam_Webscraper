#!/usr/bin/python

Cases = input()

def euclid(a, b):
    if b == 0:
        return a
    #if a == 0:
    #    return b
    if a == 1:
        return 1
    #if a < b:
    #    a, b = b, a
    return euclid(b, a % b)

for i in xrange(Cases):
    line = map(int, raw_input().split())
    n = line[0]
    nums = line[1:]
    # calculate the differences of adjacent elements
    difs = map(lambda x, y: abs(x-y), nums[:-1], nums[1:])

    # Rationale: if we find a T such that the difference of any adjacent pair
    #   of elements in `nums` is dividible by T, then the numbers in each
    #   separate pair have the same remainder (mod T). As all pairs are
    #   linked, it follows that all of `nums` have the same remainder (mod T).

    # So all we have to do is find the highest common divisor of all difs = T
    T = reduce(euclid, difs)
    # The smallest y is just what we'll add to any of `nums` to make it dividible by T
    y = -nums[0] % T

    print "Case #{0}: {1}".format(i+1, y)
