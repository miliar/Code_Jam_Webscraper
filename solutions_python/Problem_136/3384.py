#!/usr/bin/python
# -*- coding: utf-8 -*-

import linecache

file_name = './b_input.in'

def sum_list(count, C, F, X):
    sum = 0
    for x in xrange(count):
        x = x + 1
        sum += C/(2+(x-1)*F)
    return sum + X/(2+count*F)


def main():
    case_count = int(linecache.getline(file_name, 1))
    for x in xrange(case_count):
        data = linecache.getline(file_name, x+2).strip().split(' ')
        min_spent = float(data[2]) / 2
        for x_t in xrange(int(float(data[2]))):
            tmp = sum_list(x_t, float(data[0]), float(data[1]), float(data[2]))
            if tmp > min_spent:
                break
            min_spent = tmp
        print "Case #%s: %s" % (x+1, min_spent)

if __name__ == '__main__':
    main()
