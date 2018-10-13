#!/usr/bin/python

import sys
import os

def num_in_format(num):
    c = [int(d) for d in str(num)]
    clen = len(c)
    for i in range(clen-1):
        if c[i] > c[i+1]:
            return False
    return True

def calculate_output(digit):
    if (digit < 10):
        return digit

    for i in range(digit, 9, -1):
        if num_in_format(i):
            return i
    
def run():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        m = int(raw_input())
        output = calculate_output(m)
        print "Case #" + str(i) + ": " + str(output)

if __name__ == '__main__':
    run()
