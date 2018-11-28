#!/usr/bin/env python

import sys

def helper(lists):
    N = (len(lists) + 1) / 2
    nums = {}
    for l in lists:
        l_ints = [int(x) for x in l.split(' ')]
        for x in l_ints:
            if x not in nums:
                nums[x] = 0
            nums[x] += 1

    missing_nums = []
    for n in nums:
        if nums[n] % 2 != 0:
            missing_nums.append(n)

    assert len(missing_nums) == N, "Incorrect length of missing numbers"

    missing_nums.sort()
    return " ".join([str(x) for x in missing_nums])

def parse_file(num_lines=-1):
    with open(sys.argv[1], 'r') as f:
        lines = [l.rstrip('\n') for l in f.readlines()]
    i = 1
    tests = []
    varying_nlines = False
    if num_lines == -1:
        varying_nlines = True

    while i < len(lines):
        new_test = []
        if varying_nlines:
            num_lines = int(lines[i])*2 - 1
            i += 1

        for j in range(num_lines):
            new_test.append(lines[i])
            i += 1
        tests.append(new_test)
    return int(lines[0]), tests

#num_tests, tests = parse_file(num_lines=1)
num_tests, tests = parse_file()

for case,test in enumerate(tests):
    sol = helper(test)
    print 'Case #{}: {}'.format(case+1, sol)
