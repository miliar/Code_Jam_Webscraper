#!/usr/bin/env python

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())


class Go:
    def __init__(self, groups):
        self.groups = groups
        self.profit = sum(groups)

def solve():
    R, k, N = read_ints()
    queue = read_ints()
    first_go = [0] * N
    groups_count = [0] * N
    profit_before_first_go = [0] * N
    go_profit = [0] * N
    cycle_size = [0] * N
    cycle_profit = [0] * N

    total_profit = 0
    group_index = 0
    go = 1
    while go <= R:
        # is the first time that a go start in this group?
        if groups_count[group_index] == 0:
            first_go[group_index] = go
            profit_before_first_go[group_index] = total_profit
            i = group_index;
            persons = 0
            groups = 0
            while persons + queue[i] <= k and groups < N:
                persons += queue[i]
                groups += 1
                i =  (i + 1) % N
            groups_count[group_index] = groups
            go_profit[group_index] = persons
        else:
            # we find a cycle
            # have we calculated the cyle informations?
            if cycle_size[group_index] == 0:
                cycle_size[group_index] = go - first_go[group_index]
                cycle_profit[group_index] = total_profit - profit_before_first_go[group_index]
      
        # is there a cycle and we can make this cycle?
        if cycle_size[group_index] != 0 and go + cycle_size[group_index] <= R:
            times = (R - go) / cycle_size[group_index]
            total_profit += times * cycle_profit[group_index]
            go = go + times * cycle_size[group_index]
            # the group stays the same, because we have cycled
        else:
            total_profit += go_profit[group_index]
            group_index = (group_index + groups_count[group_index]) % N
            go += 1
    print total_profit


def main():
    T = read_int()
    
    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve()

if __name__ == '__main__':
    main()

