#!/usr/bin/env python
from itertools import combinations
import sys


def problem(j, fi):
    n = int(fi.readline().strip())
    strings = []
    for x in range(n):
        strings.append(fi.readline().strip())
    return n, strings

def solve(params, problem_id):
    n, strings = params

    cs = []
    for s in strings:
        schars = []
        cur_char = None
        cur_char_count = 0
        for ch in s:
            if not cur_char:
                cur_char = ch
            elif cur_char != ch:
                schars.append((cur_char, cur_char_count))
                cur_char = ch
                cur_char_count = 0
            cur_char_count += 1

        schars.append((cur_char, cur_char_count))

        cs.append(schars)


    first_line = cs[0]
    for c in cs:
        if len(c) != len(first_line):
            return 'Fegla Won'
    for i in xrange(len(first_line)):
        ch = first_line[i][0]
        if not all([ch == c[i][0] for c in cs]):
            return 'Fegla Won'

    changes = 0
    for i in xrange(len(first_line)):
        nums = [c[i][1] for c in cs]
        cnt = len(nums)
        s = sum(nums)
        x = int(float(s) / cnt)
        changes += sum([abs(j - x) for j in nums])

    return changes

if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(1, total + 1):
            print "Processing case #{0}".format(i)
            res = solve(problem(i, fi), i)
            fo.write('Case #{0}: {1}\n'.format(i, res))
            fo.flush()
