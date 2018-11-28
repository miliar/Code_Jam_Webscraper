#!/usr/bin/env python

import sys

cases = []
inp = sys.stdin.read().split('\n')

for case_num in range(int(inp[0])):
    row1 = int(inp[case_num * 10 + 1])
    arrangement1 = [[int(n) for n in inp[case_num * 10 + 2].split()]]
    arrangement1 += [[int(n) for n in inp[case_num * 10 + 3].split()]]
    arrangement1 += [[int(n) for n in inp[case_num * 10 + 4].split()]]
    arrangement1 += [[int(n) for n in inp[case_num * 10 + 5].split()]]
    row2 = int(inp[case_num * 10 + 6])
    arrangement2 = [[int(n) for n in inp[case_num * 10 + 7].split()]]
    arrangement2 += [[int(n) for n in inp[case_num * 10 + 8].split()]]
    arrangement2 += [[int(n) for n in inp[case_num * 10 + 9].split()]]
    arrangement2 += [[int(n) for n in inp[case_num * 10 + 10].split()]]
    cases.append((row1, arrangement1, row2, arrangement2))

for case_num, case in enumerate(cases, 1):
    common = filter(lambda x: x in case[3][case[2]-1], case[1][case[0]-1])
    if len(common) == 1:
        print "Case #%d: %d" % (case_num, common[0])
    elif len(common) == 0:
        print "Case #%d: Volunteer cheated!" % case_num
    else:
        print "Case #%d: Bad magician!" % case_num
