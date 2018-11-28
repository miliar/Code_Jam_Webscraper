# -*- coding: utf-8 -*-

import sys, csv, re, json, urlparse


def increasing(s):
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            return False
    return True
        
def nice(n):
    #if n.endswith('0'):
    #    n = '9' * (len(n) - 1)
    n = int(n)
    while True:
        if increasing(str(n)):
            return n
        n -= 1

def main(filename):
    lines = open(filename).read().splitlines()
    for i, line in enumerate(lines):
        if i > 0:
            n = line
            print 'Case #{}: {}'.format(i, nice(n))



if __name__ == '__main__':
    main(sys.argv[1])

