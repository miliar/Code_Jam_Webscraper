#!/usr/bin/python

import fractions;
import sys;

def diff_list(l):
    diffs = []
    last = -1
    for n in sorted(l):
        if last > 0:
            diffs.append(n - last)
        last = n
    return diffs

def diff_gcd(diffs):
    gcd = diffs.pop()
    while len(diffs) > 0:
        lol = diffs.pop()
        gcd = fractions.gcd(gcd, lol)
    return gcd

cnt = int(sys.stdin.readline())

for i in range(1,cnt+1):
    nums_raw = sys.stdin.readline().split()
    sys.stdout.write("Case #"+str(i)+": ")
    nums = []
    for j in range(1,int(nums_raw[0])+1):
        nums.append(int(nums_raw[j]))
    diffs = diff_list(nums)
    gcd = diff_gcd(diffs)
    lol = min(nums)
    if lol % gcd == 0:
        sys.stdout.write(str(0))
    else:
        sys.stdout.write(str(gcd - (lol % gcd)))
    sys.stdout.write("\n")

