#! /usr/bin/env python
# -*- coding: utf8 -*-

from scipy.misc import comb

def do_calc(a,b):
    result = 0
    counted = set()

    for i in range(a,b+1):
        if i in counted:
            continue
        cycle = calc_recycle(i,a,b)
        counted = counted.union(set(cycle))
        if len(cycle) >= 2:
#            print i, cycle
            result += comb(len(cycle),2,True)
        
    return result

def calc_recycle(num,min_limit,max_limit):
    result = [num]
    base = 10
    while num >= base:
        new_num_low = num / base
        new_num_high = num % base

        lbase = 1
        while ( new_num_low / lbase ) > 0:
            lbase *= 10
        new_num = new_num_high * lbase + new_num_low

        if new_num >= min_limit and new_num <= max_limit and new_num not in result:
            result.append(new_num)
        base *= 10
    return result

def main():
    for c in range(input()):
        a,b = map(int,raw_input().split())

        print 'Case #%d: %d'% ( c+1, do_calc(a,b)  )

if __name__ == '__main__':
    main()

