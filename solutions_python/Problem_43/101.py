#!/usr/bin/env python2.6
import sys

def convert(n, base, mapping):
    return sum(
        mapping[c] * base**p
        for p, c in enumerate(reversed(n)))

        
def find_smallest(n):
    base = max(len(set(n)), 2)
    mapping = {}

    mapping[n[0]] = 1
    
    nums = [0] + range(2, base)
    for c in n[1:]:
        if c not in mapping:
            mapping[c] = nums.pop(0)
    return convert(n, base, mapping)

        
with open(sys.argv[1], "r") as f:
    tests = int(f.readline().strip())
    numbers = [f.readline().strip() for k in range(tests)]


for i, n in enumerate(numbers):
    print "Case #%d: %s" % (i + 1, find_smallest(n))

