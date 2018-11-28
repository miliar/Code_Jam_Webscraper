#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def find_min(now, diners, opt):
    #print now
    #print diners
    max_id = diners.index(max(diners))
    max_pan = diners[max_id]
    opt = min(opt, now+max_pan)
    if max_pan == 1 or opt <= now:
        return opt

    opt_candidates = []
    for split in [2,3,5,7]:
        each = diners[max_id] / split
        if each == 0: continue
        rest = diners[max_id] - each*(split-1)
        dc = [i for i in diners]
        dc[max_id] = rest
        dc += [each]*(split-1)
        opt_candidates.append(find_min(now+split-1, dc, opt))
    return min(opt, *opt_candidates)


f_input = open(sys.argv[1])
problems = int(f_input.readline().rstrip())
for probnum in xrange(1, problems+1):
    initial_diner_num = int(f_input.readline().rstrip())
    diners = map(int, f_input.readline().rstrip().split())

    # now = 0
    # opt = max(diners)
    # while True:
    #     max_id = diners.index(max(diners))
    #     max_pan = diners[max_id]
    #     opt = min(opt, now+max_pan)
    #     if max_pan == 1:
    #         break

    #     half = diners[max_id]/2
    #     rest = diners[max_id] - half
    #     diners[max_id] = rest
    #     diners.append(half)
    #     now += 1

    opt = find_min(0, diners, max(diners))

    print("Case #{}: {}".format(probnum, opt))
