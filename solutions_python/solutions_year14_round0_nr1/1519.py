#!/usr/bin/python3

import sys

t = int(sys.stdin.readline())

for case_num in range(1, t+1):
    ans_1 = int(sys.stdin.readline())
    arrangement_1 = [list(map(int, sys.stdin.readline().strip().split())) for i in range(4)]
    ans_2 = int(sys.stdin.readline())
    arrangement_2 = [list(map(int, sys.stdin.readline().strip().split())) for i in range(4)]
    ans = set(arrangement_1[ans_1 - 1]) & set(arrangement_2[ans_2-1])
    if len(ans) == 1:
        print("Case #%d: %d" % (case_num, ans.__iter__().__next__()))
    elif len(ans) > 1:
        print("Case #%d: Bad magician!" % case_num)
    else:
        print("Case #%d: Volunteer cheated!" % case_num)
