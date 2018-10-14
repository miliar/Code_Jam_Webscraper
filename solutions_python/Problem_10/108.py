#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import copy

def main():
    t = int(raw_input())
    for i in range(t):
        line = raw_input()
        line = line.split(' ')
        p = int(line[0])
        k = int(line[1])
        l = int(line[2])
        line = raw_input()
        line = line.split(' ')
        freq = []
        orig = 0
        for j in range(l):
            freq.append(int(line[j]))
            times = (j+1) % p
            if times == 0:
                times = p
            orig += int(line[j]) * times
        order = copy(freq)
        freq.sort()
        freq.reverse()
        opt = 0
        for j in range(l):
            times = (j+1) / k
            if (j+1) % k > 0:
                times += 1
            opt += freq[j] * times
        print 'Case #%d: %d' % (i+1, opt)
    
if __name__ == '__main__':
    main()