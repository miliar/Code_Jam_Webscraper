#! /usr/bin/python
# Martin Pool
# https://code.google.com/codejam/contest/1460488/dashboard

from sys import stdin

# Can we just simply enumerate them? I think we can.
#
# nb "distinct", there might be multilpe ways to generate the same number if
# it has internal repetitions, but that doesn't count...


def generate_rotations(s):
    # Generate nontrivial rotations of s, not including s itself.
    r = []
    for i in range(1, len(s)):
        r.append(s[-i:] + s[:-i])
    return r

def find_recycled_pairs(a, b):
    # Results always ordered with the low one first.
    results = set()
    for i in range(a, b+1):
        istr = str(i)
        for rot in generate_rotations(istr):
            if rot[0] == '0':
                continue
            rot_val = int(rot)
            if rot_val <= i:
                continue
            if rot_val < a or rot_val > b:
                continue
            results.add((i, rot_val))
    return results


n_cases = int(stdin.readline())
for i in range(n_cases):
    a, b = map(int, stdin.readline().rstrip().split())
    print 'Case #%d: %d' % (i + 1, len(find_recycled_pairs(a, b)))


# Tests
assert generate_rotations('1234') == ['4123', '3412', '2341']

assert len(find_recycled_pairs(1, 9)) == 0
assert len(find_recycled_pairs(10, 40)) == 3
assert len(find_recycled_pairs(100, 500)) == 156
assert len(find_recycled_pairs(1111, 2222)) == 287

# print len(find_recycled_pairs(1000000, 2000000))

