#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
TEMPLATE = 'Case #%d: %d'
def decode(input_str):
    line = input_str.split(" ")
    A = int(line[0])
    B = int(line[1])
    return (A, B)

def make_cyclicNum(num):
    num_str = str(num)
    output = list()
    for i in xrange(1,len(num_str)):
        tmp = num_str[i:] + num_str[:i]
        if tmp != num_str and tmp[0] != '0':
            if int(tmp) > num:
                if not tmp in output:
                    output.append(tmp)
    return output

def check_number(A, B):
    output = 0
    for i in xrange(A, B+1):
        output += len(filter(lambda x: x<=B, map(int, make_cyclicNum(i))))
    return output

def main():
    filename = sys.argv[1]
    with open(filename) as r:
        T = int(r.readline())
        for i in xrange(T):
            A, B = decode(r.readline().rstrip())
            print TEMPLATE % (i + 1, check_number(A, B))

if __name__ == '__main__':
    main()
