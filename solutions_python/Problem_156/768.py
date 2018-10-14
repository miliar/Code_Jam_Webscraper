#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: work.py
# $Date: Sat Apr 11 17:16:56 2015 +0800
# $Author: jiakai <jia.kai66@gmail.com>

import Queue
import sys

class Plate(object):
    n = 0
    m = 1

    def __init__(self, n):
        self.n = int(n)

    @property
    def cost(self):
        return (self.n - 1) / self.m + 1

    def __lt__(self, rhs):
        return self.cost > rhs.cost

def solve(plates):
    plates_orig = plates
    plates = map(Plate, plates)
    queue = Queue.PriorityQueue()
    map(queue.put, plates)
    cost = max(i.cost for i in plates)
    overhead = 0
    while True:
        cur_max = [queue.get()]
        next_cost = 0
        while not queue.empty():
            v = queue.get()
            if v.cost != cur_max[0].cost:
                next_cost = v.cost
                queue.put(v)
                break
            cur_max.append(v)
        for i in cur_max:
            i.m += 1
            next_cost = max(next_cost, i.cost)
        next_cost += len(cur_max) + overhead
        if next_cost > cost:
            break
        overhead += len(cur_max)
        cost = next_cost
        map(queue.put, cur_max)

    return cost

def main():
    nr_case = int(raw_input())
    for i in range(nr_case):
        n = int(raw_input())
        p = map(int, raw_input().split())
        ans = solve(p)
        print 'Case #{}: {}'.format(i + 1, ans)
        #print >>sys.stderr, p, ans

if __name__ == '__main__':
    main()
