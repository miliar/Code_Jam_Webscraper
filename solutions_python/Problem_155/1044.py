#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: work.py
# $Date: Sat Apr 11 16:23:03 2015 +0800
# $Author: jiakai <jia.kai66@gmail.com>

def solve(data):
    ans = 0
    tot_stand = 0
    for req_other, cur_cnt in enumerate(data):
        cur_cnt = int(cur_cnt)
        if not cur_cnt:
            continue
        to_add = max(req_other - tot_stand, 0)
        ans += to_add
        tot_stand += to_add + cur_cnt
    return ans


def main():
    nr_case = int(raw_input())
    for i in range(nr_case):
        n, v = raw_input().split()
        print 'Case #{}: {}'.format(i + 1, solve(v))

if __name__ == '__main__':
    main()
