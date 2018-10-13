#!/usr/bin/env python3


def solve(smax, nums):
    clap = 0
    invite = 0
    for i, count in enumerate(nums):
        count = int(count)
        if clap < i:
            needs = i - clap
            invite += needs
            clap += needs
        clap += count
    return invite


testcases = int(input())

for case_n in range(1, testcases+1):
    #case_data = map(int, input().split())
    case_data = input().split()
    print("Case #%i: %s" % (case_n, solve(*case_data)))
