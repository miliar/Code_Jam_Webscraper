#!/usr/bin/python3

from header import *

num_tests = int(input())

for case_num in range(1, num_tests+1):
    dest, num_horses = map(int, input().split())
    times = []
    for _ in range(num_horses):
        pos, speed = map(int, input().split())
        times.append((dest - pos)/speed)

    print("Case #{}: {:.7f}".format(case_num, dest / max(times)))
    

