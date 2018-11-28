# -*- coding: utf-8 -*-
import sys
import math

def calc_denominations(C,D,V,denom_list):
    count = 0
    if 1 not in denom_list:
        denom_list.append(1)
        count += 1
    denom_list.sort()
    denom_list.append(V)
    sum = denom_list[0]

    for denom in denom_list[1:-1]:
        while sum*C+1 < denom:
            sum += sum*C+1
            count += 1
        sum += denom

    while sum*C < denom_list[-1]:
        sum += sum*C+1
        count += 1

    return count

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    test_num = int(f.readline())

    for i in xrange(1, test_num+1):
        data = map(int, f.readline().split())
        denom_list = map(int, f.readline().split())
        ans = calc_denominations(data[0], data[1], data[2], denom_list)
        print('Case #%i: %s' % (i, ans) )
