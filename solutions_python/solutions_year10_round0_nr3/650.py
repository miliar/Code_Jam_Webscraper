#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, raw_input().split())

#####################################################################

#R: The roller coaster will run R times in a day.
#k: The roller coaster can hold k people at once.

def get_profit(R, k, groups):
    
    profit = 0
    for _ in xrange(R):
        for index in xrange(len(groups) + 2):
            if sum(groups[:index]) > k: break
        index -= 1
        profit += sum(groups[:index])
        groups = groups[index:] + groups[:index]
    return profit

if __name__ == '__main__':
    
    T = readint()
    for t in xrange(1, T+1):
        R, k, _ = readlinearray(int)
        groups = readlinearray(int)
        
        profit = get_profit(R, k, groups)
        print 'Case #%d: %d' % (t, profit)
