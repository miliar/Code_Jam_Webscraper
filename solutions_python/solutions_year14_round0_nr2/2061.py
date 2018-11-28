#!/usr/bin/env python

from __future__ import division

import sys

def main():
    filename = sys.argv[1]
    sys.stdout = open(filename.replace('.in', '.out'), 'w')
    
    f = open(filename)
    cases = int(next(f))
    
    for i in xrange(1, cases + 1):
        answer = parse(f)
        print 'Case #{0}: {1}'.format(i, answer)
    
def parse(f):
    cost, farm_rate, win = map(float, next(f).strip().split(' '))
    return solve(2, cost, farm_rate, win)
    
def solve(init_rate, farm_cost, farm_rate, win_cost):
    prev_farm_time = 0
    prev_rate = init_rate
    prev_time = win_cost / init_rate
    
    num_farms = 1
    while True:
        rate = farm_rate * num_farms + init_rate
        time = prev_farm_time + farm_cost / prev_rate
        
        prev_farm_time = time
        prev_rate = rate
        num_farms += 1
        
        new_time = time + win_cost / rate
        
        if new_time >= prev_time:
            return prev_time
        else:
            prev_time = new_time
            
        
    
        
if __name__ == '__main__':
    main()
    
    